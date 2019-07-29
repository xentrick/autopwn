#!/usr/bin/env python3

from multiprocessing.dummy import Pool as ThreadPool

from . import services
from . import util

import logging

log = logging.getLogger(__name__)


class Autopwn(object):
    def __init__(self, numThreads=8):
        log.info("Starting Autopwn!")

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
        log.debug(f"Verifying host: {host}")
        util.ip.checkIP(host)
        if not self.ssh.service(host):
            log.debug(f"Host not eligible {host}")
            return

        log.info(f"Scoring {host}")
        self.chat.run(host)
        self.drupal.run(host)
        self.payroll.run(host)
        self.phpmyadmin.run(host)
        self.proftpd.run(host)
        self.samba.run(host)
        self.webrick.run(host)

    def scan(self, IP):
        """ Threaded scan function to see what hosts are up and eligible """
        return self.ssh.service(IP)
        # tmpSSH = services.SSH()
        # tmpSSH.service(IP)

    def checkAll(self, ipList):
        log.info("[-] Powering up the lasers. Preparing for world domination!")
        log.info("[+] Scanning for available boxes to exploit")
        self.__threads.map(self.scoreHost, ipList)
