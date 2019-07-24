

from .base import Service

import logging

log = logging.getLogger(__name__)


class PHPMyAdmin(Service):
    def __init__(self):

        self.name = "PHPMyAdmin"
        self.protocols = ["HTTP"]
        self.ports = [8585]
        self.exploits = ["multi/http/phpmyadmin_preg_replace"]
        self.creds = {"root": ""}
        self.cves = ["CVE-2013-3238"]
        super().__init__()
