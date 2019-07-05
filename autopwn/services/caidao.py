#!/usr/bin/env python3

from .base import Service
from ..const import creds

import logging
log = logging.getLogger(__name__)


class Caidao(Service):

    def __init__(self):

        self.name = "Chinese Caidao"

        self.protocols = [
            "HTTP"
        ]

        self.ports = [
            80
        ]

        self.exploits = [
            "auxiliary/scanner/http/caidao_bruteforce_login"
        ]

        self.creds = creds

        self.cves = []
