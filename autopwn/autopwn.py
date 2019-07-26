#!/usr/bin/env python3

from . import services
from . import util

import logging
log = logging.getLogger(__name__)


class Autopwn(object):
    def __init__(self):
        log.info("Starting Autopwn!")

        self.chat = services.Chat()
        self.drupal = services.Drupal()
        self.payroll = services.Payroll()
        self.phpmyadmin = services.PHPMyAdmin()
        self.proftpd = services.ProFTPD()
        self.samba = services.Samba()
        self.webrick = services.Webrick()

    def scoreHost(self, host):
        log.debug("Verifying host IP")
        util.ip.checkIP(host)

        log.debug(f"SSH Acid test {host}")
        util.acid.ssh_test(host)

        log.info("Scoring {}".format(host))
        self.mysql.exploitall(host)


    def checkAll(self):
        log.info("Powering up the lasers. Preparing for world domination!")
        return
