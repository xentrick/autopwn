#!/usr/bin/env python3

from multiprocessing.dummy import Pool as ThreadPool

from . import services
from . import util

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Autopwn(object):
    def __init__(self, numThreads=8, debug=False):
        log.info("[-] Starting Autopwn!")
        self._debug = debug
        if not self._debug:
            self.__ctf = util.ctfd.Scoring()

        self.chat = services.Chat()
        self.drupal = services.Drupal()
        self.payroll = services.Payroll()
        self.phpmyadmin = services.PHPMyAdmin()
        self.proftpd = services.ProFTPD()
        self.samba = services.Samba()
        self.ssh = services.SSH()
        self.webrick = services.Webrick()

        self.__threads = ThreadPool(numThreads)

    def scoreHost(self, host):
        log.debug(f"[-] Verifying host: {host}")
        util.ip.checkIP(host)
        __teamid = util.team.eligible(host)
        if not __teamid:
            return

        log.info(f"[+] Scoring {__teamid} ({host})")
        if self._debug:
            self.chat.run(host)
            self.drupal.run(host)
            self.payroll.run(host)
            self.phpmyadmin.run(host)
            self.proftpd.run(host)
            self.samba.run(host)
            self.webrick.run(host)
        else:
            if not self.chat.run(host):
                self.__ctf.award(__teamid, "Chat")
            if not self.drupal.run(host):
                self.__ctf.award(__teamid, "Drupal")
            if not self.payroll.run(host):
                self.__ctf.award(__teamid, "Payroll")
            if not self.phpmyadmin.run(host):
                self.__ctf.award(__teamid, "PHPMyAdmin")
            if not self.proftpd.run(host):
                self.__ctf.award(__teamid, "ProFTPD")
            if not self.samba.run(host):
                self.__ctf.award(__teamid, "Samba")
            if not self.webrick.run(host):
                self.__ctf.award(__teamid, "Webrick")

    def checkAll(self, ipList):
        log.info("[-] Powering up the lasers. Preparing for world domination!")
        log.info("[+] Scanning for available boxes to exploit")
        self.__threads.map(self.scoreHost, ipList)
