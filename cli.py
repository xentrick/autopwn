#!/usr/bin/env python3

from autopwn import Autopwn
from pprint import pprint

import logging
logging.basicConfig(level=logging.DEBUG)

pwn = Autopwn()

tar = "192.168.13.152"

# MySQL
pprint(pwn.mysql.msfcore())
print(pwn.mysql.name)
