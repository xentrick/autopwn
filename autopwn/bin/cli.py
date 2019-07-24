

import logging
from pprint import pprint

from autopwn import Autopwn

log = logging.getLogger("autopwn")
log.setLevel(logging.DEBUG)

def main():
    pwn = Autopwn()

    tar = "192.168.13.152"

    # MySQL
    pprint(pwn.mysql.msfcore())
    print(pwn.mysql.name)
    #pprint(pwn.mysql.search())
    pprint(pwn.mysql.search("mysql"))

    pwn.scoreHost(tar)

