#!/usr/bin/env python3

from .base import Service

import logging

log = logging.getLogger(__name__)


class WebDAV(Service):
    def __init__(self):

        super().__init__(self)

        self.name = "WebDAV"

        self.protocols = ["HTTP"]

        self.ports = [8585]

        self.exploits = ["auxiliary/scanner/http/http_put"]

        self.creds = {}

        self.cves = []
