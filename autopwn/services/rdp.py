

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class RDP(Service):
    def __init__(self, autopwn):

        super(RDP, self).__init__(autopwn)

        self.name = "Remote Desktop Protocol"
        self.protocols = ["RDP"]
        self.ports = [3389]
        self.exploits = [
            # FIX IT
        ]
        self.creds = creds
        self.cves = []
