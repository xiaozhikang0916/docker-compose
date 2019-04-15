#!/usr/bin/env python

import os
import random
import string

ARIA_NG_VERSION = '1.0.3'
env = """ARIA2_TOKEN={ARIA2_TOKEN}
BGMI_TOKEN={BGMI_TOKEN}
LOCAL_TZ=Asia/Shanghai
PORT=8888
        
HOST_BGMI_PATH=./data
UID={UID}
GID={GID}
"""


def main():
    ariang_zip_name = "AriaNg-{}.zip".format(ARIA_NG_VERSION)
    if not os.path.exists('ariang'):
        if os.path.exists(ariang_zip_name):
            os.remove(ariang_zip_name)
        os.system('wget https://github.com/mayswind/AriaNg/releases'
                  '/download/{0}/AriaNg-{0}.zip'.format(ARIA_NG_VERSION))
        os.system('unzip {} -d ariang'.format(ariang_zip_name))
    if not os.path.exists('.env'):
        with open('.env', 'w+', encoding='utf8') as f:
            ARIA2_TOKEN = random_string(8)
            BGMI_TOKEN = random_string(16)
            f.write(env.format(ARIA2_TOKEN=ARIA2_TOKEN,
                               BGMI_TOKEN=BGMI_TOKEN,
                               UID=os.getuid(),
                               GID=os.getgid()))

        os.system('docker-compose up -d')
        print('docker compose running in background with bgmi admin token '
                  + ARIA2_TOKEN + ',bgmi admin token ' + BGMI_TOKEN)


def random_string(length):
    return ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    )


if __name__ == '__main__':
    main()
