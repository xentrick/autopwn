#!/usr/bin/env python3

from autopwn import Autopwn
from pprint import pprint

import logging
log = logging.getLogger("autopwn")
log.setLevel(logging.DEBUG)
msflog = logging.getLogger("pymetasploit3")
msflog.setLevel(logging.DEBUG)


pwn = Autopwn()

#tar = "192.168.13.152"
tar = "192.168.56.3"

# MySQL
pprint(pwn.mysql.msfcore())
print(pwn.mysql.name)
#pprint(pwn.mysql.search())
pprint(pwn.mysql.search("mysql"))

pwn.scoreHost(tar)

