#!/usr/bin/env python3

import socket
from pymetasploit3.msfrpc import MsfRpcClient

import logging

log = logging.getLogger(__name__)


class Service(object):
    def __init__(self):
        self._msfuser = "talosvillage"
        self._msfpass = "T4L05PWN5U"
        self._msfrpcd = MsfRpcClient(
            self._msfpass,
            username=self._msfuser,
            ssl=True,
            server="127.0.0.1",
            port=55553,
        )

    def msfcore(self):
        """ Return Modules in MsfRpcClient """
        return [m for m in dir(self._msfrpcd) if not m.startswith("_")]

    def exploit(self, module):
        pwn = self._msfrpcd.use("exploits", module)
        log.info("{} fired!".format(pwn.name))

    def exploitall(self):
        for i in self.exploits:
            self.exploit(i)

    def login(self):
        return

    def status(self, ip):
        # TCP
        if "TCP" in self.protocols:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for p in self.ports:
                try:
                    s.connect((ip), p)
                    return True
                except socket.error:
                    raise Exception(
                        "{ip}: {name} is down on port {port}".format(
                            ip=ip, name=self.name, port=p
                        )
                    )

    def shells(self):
        """ List sessions """
        return

    def attach(self):
        """ Attach to a session"""
        return

    def detach(self):
        """ Kill a session """
        return

    """ Properties """

    @property
    def auxiliary(self):
        return self._msfrpcd.modules.auxiliary

    @property
    def encoders(self):
        self._msfrpcd.modules.encoders

    @property
    def nops(self):
        self._msfrpcd.modules.nops

    @property
    def payloads(self):
        self._msfrpcd.modules.payloads

    @property
    def post(self):
        self._msfrpcd.modules.post
