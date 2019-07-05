#!/usr/bin/env python3

from .base import Service

import logging
log = logging.getLogger(__name__)


class ManageEngine(Service):

    def __init__(self):

        self.name = "ManageEngine"

        self.protocols = [
            "HTTP"
        ]

        self.ports = [
            8020
        ]

        self.exploits = [
            "exploit/windows/http/manageengine_connectionid_write"
        ]

        self.creds = {
            "admin": "admin"
        }

        self.cves = [
            "CVE-2015-8249"
        ]
