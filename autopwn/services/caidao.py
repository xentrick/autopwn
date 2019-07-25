

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class Caidao(Service):
    def __init__(self, autopwn):

        super(Caidao, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "Chinese Caidao"
        self.protocols = ["HTTP"]
        self.ports = [80]
        self.exploits = ["auxiliary/scanner/http/caidao_bruteforce_login"]
        self.creds = creds
        self.cves = []
