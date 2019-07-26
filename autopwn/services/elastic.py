

from .base import Service

import logging

log = logging.getLogger(__name__)


class Elastic(Service):
    def __init__(self, autopwn):

        super(Elastic, self).__init__(autopwn)

        self.name = "Elastic Search"
        self.protocols = ["HTTP"]
        self.ports = 9200
        self.exploits = ["exploit/multi/elasticsearch/script_mvel_rce"]
        self.creds = {}
        self.cves = ["CVE-2014-3120"]
