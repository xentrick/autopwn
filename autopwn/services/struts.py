#!/usr/bin/env python3

from .base import Service

import logging

log = logging.getLogger(__name__)


class Struts(Service):
    def __init__(self):

        super().__init__(self)

        self.name = "Apache Struts"

        self.protocols = ["HTTP"]

        self.ports = [8282]

        self.exploits = ["exploit/multi/http/struts_dmi_rest_exec"]

        self.creds = {"sploit": "sploit"}

        self.cves = ["CVE-2016-3087"]
