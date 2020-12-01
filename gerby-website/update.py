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

diff = subprocess.Popen(['git', 'diff', 'master:document.tex', '--', '../document.tex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = diff.communicate()

log.info(out)
log.error(err)

if not err:
    pull = subprocess.Popen(['git', 'pull', 'origin', 'master'], cwd='/root/mipstar/', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = pull.communicate()
    log.info(o)
    log.error(e)

    if out:
        gen_tags = subprocess.Popen(['python3', 'tagger.py', 'document.tex', '>', 'tags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
        o, e = gen_tags.communicate()
        log.info(o)
        log.error(e)

        gen_doc = subprocess.Popen(['plastex', '--renderer=Gerby', './document.tex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/root/mipstar/')
        o, e = gen_doc.communicate()
        log.info(o)
        log.error(e)

        update = subprocess.Popen(['python3', 'update.py'], cwd='/root/mipstar/gerby-website/gerby/', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = update.communicate()
        log.info(o)
        log.error(e)

    restart = subprocess.Popen(['sudo', 'systemctl', 'restart', 'mipstar'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = restart.communicate(input=bytes(AUTH, 'utf-8'))

    log.info(o)
    log.error(e)

    print('hi still here guys')