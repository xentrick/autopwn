#!/usr/bin/env python3

from .base import Service

import logging
log = logging.getLogger(__name__)


class ProFTPD(Service):
    def __init__(self, autopwn):

        super(ProFTPD, self).__init__(autopwn)

        self.name = "ProFTPD 1.3.5"
        self.protocols = "TCP"
        self.ports = [21]
        self.creds = []
        self.cves = ["CVE-2015-3306"]
        self.exploits = [
            "exploit/unix/ftp/proftpd_modcopy_exe"
        ]
        self.payload = "cmd/unix/reverse_perl"
        self.verify = "whoami"
