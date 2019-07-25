

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class RDP(Service):
    def __init__(self, autopwn):

        super(RDP, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "Remote Desktop Protocol"
        self.protocols = ["RDP"]
        self.ports = [3389]
        self.exploits = [
            # FIX IT
        ]
        self.creds = creds
        self.cves = []
