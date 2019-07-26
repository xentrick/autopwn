

from .base import Service

import logging

log = logging.getLogger(__name__)


class JMX(Service):
    def __init__(self, autopwn):

        super(JMX, self).__init__(autopwn)

        self.name = "Java JMX Server"
        self.protocols = ["TCP"]
        self.ports = 1617
        self.exploits = ["multi/misc/java_jmx_server"]
        self.creds = {}
        self.cves = ["CVE-2015-2342"]
        self.msfopts = {
            "RHOSTS": None,
            "RPORT": self.ports
        }
