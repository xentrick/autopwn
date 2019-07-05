#!/usr/bin/env python3

from .base import Service
from ..const import creds

import logging
log = logging.getLogger(__name__)


class PSExec(Service):

    def __init__(self):

        self.name = "psexec"

        self.protocols = [
            "SMB",
            "NetBIOS"
        ]

        self.ports = [
            139,
            445
        ]

        self.exploits = [
            "exploits/windows/smb/psexec",
            "exploits/windows/smb/psexec_psh"
        ]

        self.creds = creds

        self.cves = []
