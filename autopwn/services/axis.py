

from .base import Service

import logging

log = logging.getLogger(__name__)


class Axis(Service):
    def __init__(self, autopwn):

        super(Axis, self).__init__(autopwn)

        self.name = "Apache Axis2"
        self.protocols = ["HTTP"]
        self.ports = 8282
        self.exploits = [
            "exploit/multi/http/axis2_deployer"
        ]
        self.creds = {}
        self.cves = ["CVE-2010-0219"]
