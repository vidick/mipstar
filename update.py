import os
import sys
import argparse
import logging
from dotenv import load_dotenv
import paramiko
from progress.spinner import Spinner
from utils import get_chapters

load_dotenv()
AUTH = str(os.getenv('AUTH'))
args = None

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('134.122.114.22', username='root', password=AUTH)

logging.basicConfig(stream=sys.stdout)
log = logging.getLogger('Boostrapper')
log.setLevel(logging.INFO)


def check_errors(keywords, output):
    """Check if outputs returned any errors/exceptions."""
    for word in keywords:
        if word in output:
            return True
    return False


def log_outputs(logger, out, err, prepend_out='', prepend_err=''):
    """Log output and error messages to console."""
    if out:
        combined = ''.join(out)
        if check_errors(['ERROR', 'Error'], combined):
            raise RuntimeError('Error rendering website')
        logger.info(prepend_out + combined)
    if err:
        combined = ''.join(err)
        if check_errors(['ERROR', 'Error'], combined):
            raise RuntimeError('Error rendering website')
        logger.info(prepend_err + combined)


def update_website(pull_latest):
    if pull_latest:
        log.info('  Checking diff between local and remote tex files')
        stdin, stdout, stderr = ssh.exec_command(
            'cd /root/mipstar && git fetch --prune')
        log_outputs(log, stdout.readlines(), stderr.readlines(), '', '\n')

    _, chapters = get_chapters()
    chapters.append('preamble.tex')

    out = []
    err = []

    if pull_latest:
        for chapter in chapters:
            stdin, stdout, stderr = ssh.exec_command(
                f'cd /root/mipstar && git diff origin/master:latex/{chapter} -- latex/{chapter}')
            out += stdout.readlines()
            err += stderr.readlines()
        log_outputs(log, out, err, '', '\n')

        log.info('  Merging from remote master branch')
        stdin, stdout, stderr = ssh.exec_command(
            'cd /root/mipstar && git merge origin/master')
        log_outputs(log, stdout.readlines(), stderr.readlines(), '\n', '\n')

    if out or args.force or not pull_latest or any('No such file or directory' in msg for msg in err):
        log.info('  Updating document tags')
        stdin, stdout, stderr = ssh.exec_command(
            'cd /root/mipstar && python3 make_doc.py && python3 tagger.py ./latex/make_doc.tex > tags')
        log_outputs(log, stdout.readlines(), stderr.readlines())

        log.info('  Rendering make_doc.tex using plastex')
        stdin, stdout, stderr = ssh.exec_command(
            'cd /root/mipstar/latex && plastex --renderer=Gerby ./make_doc.tex')
        stdin.write('y\n')

        spinner = Spinner('Working ')
        while not stdout.channel.exit_status_ready():
            spinner.next()
        spinner.finish()

        log_outputs(log, stdout.readlines(), stderr.readlines())

        if not args.nopdf or (args.force and not args.nopdf):
            log.info('  Making book.tex')
            stdin, stdout, stderr = ssh.exec_command(
                'cd /root/mipstar && python3 make_book.py')
            log_outputs(log, stdout.readlines(), stderr.readlines())

            log.info('  Adding margin notes/tags to .tex files')
            stdin, stdout, stderr = ssh.exec_command(
                'cd /root/mipstar && python3 pdf_tagger.py')
            log_outputs(log, stdout.readlines(), stderr.readlines())

            log.info('  Generating PDFs')
            stdin, stdout, stderr = ssh.exec_command(
                'cd /root/mipstar && python3 make_pdfs.py')

            spinner = Spinner('Working ')
            while not stdout.channel.exit_status_ready():
                spinner.next()
            spinner.finish()

            log_outputs(log, [], stderr.readlines())
        else:
            log.info('  Skipping PDF generation')

        if not args.skippreview:
            log.info('  Adding page previews')
            stdin, stdout, stderr = ssh.exec_command(
                'cd /root/mipstar && python3 add_previews.py')
            log_outputs(log, stdout.readlines(), stderr.readlines())
        else:
            log.info('  Skipping page preview generation')

        log.info('  Deleting old database file')
        stdin, stdout, stderr = ssh.exec_command(
            'cd /root/mipstar/gerby-website/gerby/tools && rm tags.sqlite')
        log_outputs(log, stdout.readlines(), stderr.readlines())

        log.info('  Updating database with new tags')
        stdin, stdout, stderr = ssh.exec_command(
            'cd /root/mipstar/gerby-website/gerby/tools && python3 update.py')

        spinner = Spinner('Working ')
        while not stdout.channel.exit_status_ready():
            spinner.next()
        spinner.finish()

        log_outputs(log, stdout.readlines(), stderr.readlines())
    else:
        log.info('  No diff found')

    log.info('  Requesting service restart')
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl restart mipstar')
    stdin.write(AUTH + '\n')
    log_outputs(log, stdout.readlines(), stderr.readlines())

    ssh.close()


def restore_previous():
    _, stdout, stderr = ssh.exec_command('cd /root/mipstar && cat backup')
    if stderr:
        return

    back_num = int(stdout.readline())
    log.info('  Restoring previous stable commit')
    _, stdout, stderr = ssh.exec_command(
        f'cd /root/mipstar && git reset --hard HEAD~{back_num + 1}')
    log_outputs(log, stdout.readlines(), stderr.readlines(), '\n', '\n')

    log.info('  Update backup')
    _, stdout, stderr = ssh.exec_command(
        f'cd /root/mipstar && echo {back_num + 1} > backup')

    update_website(pull_latest=False)


parser = argparse.ArgumentParser(
    description='Pull changes from GitHub and update mipstar.net.')
parser.add_argument(
    '-np', '--nopdf', help='skip PDF generation step', action='store_true')
parser.add_argument(
    '-f', '--force', help='force tag and database regeneration', action='store_true')
parser.add_argument('-skpp', '--skippreview',
                    help='skip page preview generation', action='store_true')
args = parser.parse_args()

try:
    update_website(pull_latest=True)
except RuntimeError:
    restore_previous()
