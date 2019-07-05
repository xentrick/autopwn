#!/usr/bin/env python3

import logging
log = logging.getLogger(__name__)


class Service(object):

    def __init__(self):

        self.protocols = []
        self.ports = []
        self.exploits = []
        self.creds = {}

    def exploit(self):
        return

    def login(self):
        return

    def status(self):
        return
