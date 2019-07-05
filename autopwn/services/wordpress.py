#!/usr/bin/env python3

from .base import Service

import logging
log = logging.getLogger(__name__)


class WordPress(Service):

    def __init__(self):

        self.name = "WordPress"

        self.protocols = [
            "HTTP"
        ]

        self.ports = [
            8585
        ]

        self.exploits = [
            "unix/webapp/wp_ninja_forms_unauthenticated_file_upload"
        ]

        self.creds = {}

        self.cves = [
            "CVE-2016-1209"
        ]
