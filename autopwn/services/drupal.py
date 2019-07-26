#!/usr/bin/env python3

from .base import Service

import logging
log = logging.getLogger(__name__)


class Drupal(Service):
    def __init__(self, autopwn):

        super(Drupal, self).__init__(autopwn)

        self.name = "Drupal 7.x"
        self.protocols = "TCP"
        self.ports = [21]
        self.creds = []
        self.cves = ["CVE-2014-3704"]
        self.exploits = [
            "exploit/multi/http/drupal_drupageddon"
        ]
        self.payload = "php/reverse_perl"
        self.verify = "whoami"
