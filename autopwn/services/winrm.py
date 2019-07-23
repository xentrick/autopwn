#!/usr/bin/env python3

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class WinRM(Service):
    def __init__(self):

        self.name = "Windows Remote Management service"
        self.protocols = ["HTTPS"]
        self.ports = [5985]
        self.exploits = [
            "exploits/windows/winrm/winrm_script_exec",
            "auxiliary/scanner/winrm/winrm_cmd",
            "auxiliary/scanner/winrm/winrm_wql",
            "auxiliary/scanner/winrm/winrm_login",
            "auxiliary/scanner/winrm/winrm_auth_method",
        ]
        self.creds = creds
        self.cves = []
        super(WinRM).__init__()
