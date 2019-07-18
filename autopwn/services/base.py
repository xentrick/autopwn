#!/usr/bin/env python3

import socket

import logging

log = logging.getLogger(__name__)


class Service(object):
    def __init__(self):

        self.name = "Base Service Class"
        self.protocols = []
        self.ports = []
        self.exploits = []
        self.creds = {}
        self.cves = []

    def exploit(self):
        return

    def login(self):
        return

    def status(self, ip=None):
        # TCP
        if "TCP" in self.protocols:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for p in self.ports:
                try:
                    s.connect((ip), p)
                except:
                    raise Exception(
                        "{ip}: {name} is down on port {port}".format(
                            ip=ip, name=self.name, port=p
                        )
                    )
