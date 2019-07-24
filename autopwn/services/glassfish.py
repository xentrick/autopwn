

from .base import Service

import logging

log = logging.getLogger(__name__)


class GlassFish(Service):
    def __init__(self):

        self.name = "GlassFish"
        self.protocols = ["HTTP", "HTTPS"]
        self.ports = [4848, 8080, 8181]
        self.exploits = [
            "exploits/multi/http/glassfish_deployer",
            "auxiliary/scanner/http/glassfish_login",
        ]
        self.cves = ["CVE-2011-0807"]
        super().__init__()
