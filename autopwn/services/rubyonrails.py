#!/usr/bin/env python3

from .base import Service

import logging

log = logging.getLogger(__name__)


class RubyonRails(Service):
    def __init__(self):

        super().__init__(self)

        self.name = "Ruby on Rails"

        self.protocols = ["HTTP"]

        self.ports = [3000]

        self.exploits = ["exploit/multi/http/rails_web_console_v2_code_exec"]

        self.creds = {}

        self.cves = ["CVE-2015-3224"]
