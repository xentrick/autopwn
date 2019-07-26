

from .base import Service

import logging

log = logging.getLogger(__name__)


class PHPMyAdmin(Service):
    def __init__(self, autopwn):

        super(PHPMyAdmin, self).__init__(autopwn)

        self.name = "PHPMyAdmin"
        self.protocols = ["HTTP"]
        self.ports = 80 #8585
        self.exploits = ["exploit/multi/http/phpmyadmin_preg_replace"]
        self.creds = {"root": ""}
        self.cves = ["CVE-2013-3238"]
        self.msfopts = {
            "RHOSTS": None,
            "RPORT": self.ports
        }
