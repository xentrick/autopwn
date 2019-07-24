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

    def exploit(self, module, host):
        log.debug("Preparing exploit for {}".format(self.name))
        # Split module type and path
        mType, mPath = module.split("/", 1)
        log.debug("Module Type: {}".format(mType))
        log.debug("Module Path: {}".format(mPath))
        pwn = self._msfrpcd.use("exploits", module)
        log.info("{} fired!".format(pwn.name))

    def exploitall(self, host):
        log.debug("Sending all exploits for {}".format(self.name))
        for i in self.exploits:
            self.exploit(i, host)

    def login(self):
        return

    def status(self, ip):
        """ Some sort of base for checking service status """
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

    """ Helpers """

    def search(self, keyword=None):
        if keyword:
            if not isinstance(keyword, str):
                return TypeError("Search keyword must be a string.")
            return [s for s in self._msfrpcd.modules.exploits if keyword.lower() in s]
        return self._msfrpcd.modules.exploits

    """ Properties """

    @property
    def auxiliary(self):
        return self._msfrpcd.modules.auxiliary

    @property
    def encoders(self):
        return self._msfrpcd.modules.encoders

    @property
    def nops(self):
        return self._msfrpcd.modules.nops

    @property
    def payloads(self):
        return self._msfrpcd.modules.payloads

    @property
    def post(self):
        return self._msfrpcd.modules.post

