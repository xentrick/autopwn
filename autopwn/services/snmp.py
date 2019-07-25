

from .base import Service

import logging

log = logging.getLogger(__name__)


class SNMP(Service):
    def __init__(self, autopwn):

        super(SNMP, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "SNMP"
        self.protocols = ["UDP"]
        self.ports = [161]
        self.exploits = ["auxiliary/scanner/snmp/snmp_enum"]
        self.creds = ["public"]
