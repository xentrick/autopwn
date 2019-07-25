

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class PSExec(Service):
    def __init__(self, autopwn):

        super(PSExec, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "psexec"
        self.protocols = ["SMB", "NetBIOS"]
        self.ports = [139, 445]
        self.exploits = [
            "exploits/windows/smb/psexec",
            "exploits/windows/smb/psexec_psh",
        ]
        self.creds = creds
        self.cves = []
