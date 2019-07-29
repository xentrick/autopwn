#!/usr/bin/env python3

from autopwn import Autopwn
from pprint import pprint

import logging

log = logging.getLogger("Autopwn").setLevel(logging.DEBUG)
url = logging.getLogger("urllib3")
url.setLevel(logging.WARNING)
smblog = logging.getLogger("SMB")
smblog.setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)


pwn = Autopwn()

tar = "192.168.56.4"

pwn.checkAll()

# pwn.chat.run(tar)
# pwn.drupal.run(tar)
# pwn.payroll.run(tar)
# pwn.phpmyadmin.run(tar)
# pwn.proftpd.run(tar) # What's happenin?
# pwn.samba.run(tar)
# pwn.webrick.run(tar)
