

from .base import Service

import logging

log = logging.getLogger(__name__)


class Axis(Service):
    def __init__(self, autopwn):

        super(Axis, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "Apache Axis2"
        self.protocols = ["HTTP"]
        self.ports = 8282
        self.exploits = [
            "exploit/multi/http/axis2_deployer"
        ]
        self.creds = {}
        self.cves = ["CVE-2010-0219"]
