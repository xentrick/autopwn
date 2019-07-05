#!/usr/bin/env python3

from .base import Service

import logging
log = logging.getLogger(__name__)


class MySQL(Service):

    def __init__(self):

        super().__init__(self)

        self.name = "MySQL"

        self.protocols = [
            "TCP"
        ]

        self.ports = [
            3306
        ]

        self.exploits = [
            "windows/mysql/mysql_payload",
        ]

        self.creds = {
            "root": ""
        }

        self.cves = []
