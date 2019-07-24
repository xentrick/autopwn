#!/usr/bin/env python3

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class IIS(Service):
    def __init__(self):

        self.name = "IIS HTTP/FTP"
        self.protocols = ["FTP", "HTTP"]
        self.ports = [21, 80]
        self.exploits = [
            "auxiliary/scanner/ftp/ftp_login",
            "auxiliary/dos/http/ms15_034_ulonglongadd",
        ]
        self.creds = {"vagrant": "vagrant"}
        # Uses Windows creds as well. Pull in constant values
        self.creds.update(creds)
        self.cves = ["CVE-2015-1635"]
        super().__init__()
