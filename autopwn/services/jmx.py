#!/usr/bin/env python3

from .base import Service

import logging

log = logging.getLogger(__name__)


class JMX(Service):
    def __init__(self):

        self.name = "Java JMX Server"
        self.protocols = ["TCP"]
        self.ports = [1617]
        self.exploits = ["multi/misc/java_jmx_server"]
        self.creds = {}
        self.cves = ["CVE-2015-2342"]
        super(JMX).__init__()
