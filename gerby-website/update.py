import os
import sys
import subprocess
import logging
from dotenv import load_dotenv


load_dotenv()
AUTH = str(os.getenv('AUTH'))

logging.basicConfig(stream=sys.stdout)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

print(subprocess.call(['pwd']))

diff = subprocess.Popen(['git', 'diff', 'master:document.tex', '--', 'document.tex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
out, err = diff.communicate()

if out:
    log.info(out)
if err:
    log.error(err)

if not err:
    pull = subprocess.Popen(['git', 'pull', 'origin', 'master'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
    o, e = pull.communicate()
    if o:
        log.info(o)
    if e:
        log.error(e)

    if out:
        gen_tags = subprocess.Popen(['python3', 'tagger.py', 'document.tex', '>', 'tags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
        o, e = gen_tags.communicate()
        if o:
            log.info(o)
        if e:
            log.error(e)

        gen_doc = subprocess.Popen(['plastex', '--renderer=Gerby', './document.tex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
        o, e = gen_doc.communicate()
        if o:
            log.info(o)
        if e:
            log.error(e)

        update = subprocess.Popen(['python3', 'update.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/gerby-website/gerby/')
        o, e = update.communicate()
        if o:
            log.info(o)
        if e:
            log.error(e)

    restart = subprocess.Popen(['sudo', 'systemctl', 'restart', 'mipstar'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
    o, e = restart.communicate(input=bytes(AUTH, 'utf-8'))

    if o:
        log.info(o)
    if e:
        log.error(e)

    print('hi still here guys')