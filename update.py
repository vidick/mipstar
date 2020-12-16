import os
import sys
import subprocess
import logging
from dotenv import load_dotenv
import paramiko
from progress.spinner import Spinner
from utils import *

load_dotenv()
AUTH = str(os.getenv('AUTH'))

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('134.122.114.22', username='root', password=AUTH)

logging.basicConfig(stream=sys.stdout)
log = logging.getLogger('Boostrapper')
log.setLevel(logging.INFO)

# diff = subprocess.Popen(['git', 'diff', 'master:document.tex', '--', 'document.tex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
# out, err = diff.communicate()
log.info('  Checking diff between local and remote tex files')
stdin, stdout, stderr = ssh.exec_command('cd /root/mipstar && git fetch --prune')
log_outputs(log, stdout.readlines(), stderr.readlines(), '', '\n')

_, chapters = get_chapters()

out = []
err = []
for chapter in chapters:
    stdin, stdout, stderr = ssh.exec_command(f'cd /root/mipstar && git diff origin/master:{chapter} -- {chapter}')
    out += stdout.readlines()
    err += stderr.readlines()
log_outputs(log, out, err, '', '\n')

# if not err:
    # pull = subprocess.Popen(['git', 'pull', 'origin', 'master'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
    # o, e = pull.communicate()
if out or any('No such file or directory' in msg for msg in err):
    log.info('  Updating PDFs')
    subprocess.run(['python3', 'pdf_tagger.py'])
    subprocess.run(['python3', 'make_pdfs.py'])


log.info('  Merging from remote master branch')
stdin, stdout, stderr = ssh.exec_command('cd /root/mipstar && git merge origin/master')
log_outputs(log, stdout.readlines(), stderr.readlines(), '\n', '\n')

if out or any('No such file or directory' in msg for msg in err):
    # gen_tags = subprocess.Popen(['python3', 'tagger.py', 'document.tex', '>', 'tags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
    # o, e = gen_tags.communicate()
    log.info('  Updating document tags')
    stdin, stdout, stderr = ssh.exec_command('cd /root/mipstar && python3 make_doc.py && python3 tagger.py make_doc.tex > tags')
    log_outputs(log, stdout.readlines(), stderr.readlines())

    # gen_doc = subprocess.Popen(['plastex', '--renderer=Gerby', './document.tex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
    # o, e = gen_doc.communicate()
    log.info('  Rendering make_doc.tex using plastex')
    stdin, stdout, stderr = ssh.exec_command('cd /root/mipstar && plastex --renderer=Gerby ./make_doc.tex')
    stdin.write('y\n')

    spinner = Spinner('Working ')
    while not stdout.channel.exit_status_ready():
        spinner.next()
    spinner.finish()

    log_outputs(log, stdout.readlines(), stderr.readlines())

    log.info('  Deleting old database file')
    stdin, stdout, stderr = ssh.exec_command('cd /root/mipstar/gerby-website/gerby/tools && rm hello-world.sqlite')
    log_outputs(log, stdout.readlines(), stderr.readlines())

    # update = subprocess.Popen(['python3', 'update.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/gerby-website/gerby/')
    # o, e = update.communicate()
    log.info('  Updating database with new tags')
    stdin, stdout, stderr = ssh.exec_command('cd /root/mipstar/gerby-website/gerby/tools && python3 update.py')

    spinner = Spinner('Working ')
    while not stdout.channel.exit_status_ready():
        spinner.next()
    spinner.finish()

    log_outputs(log, stdout.readlines(), stderr.readlines())
else:
    log.info('  No diff found')
# restart = subprocess.Popen(['sudo', 'systemctl', 'restart', 'mipstar'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
# o, e = restart.communicate(input=bytes(AUTH, 'utf-8'))
log.info('  Requesting service restart')
stdin, stdout, stderr = ssh.exec_command('sudo systemctl restart mipstar')
stdin.write(AUTH + '\n')
log_outputs(log, stdout.readlines(), stderr.readlines())

ssh.close()