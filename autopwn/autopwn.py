#!/usr/bin/env python3

from . import services
from . import util

import logging
log = logging.getLogger(__name__)


class Autopwn(object):
    def __init__(self):
        log.info("Starting Autopwn!")

        # msfrpcd instance
        self._msfrpcd = util.msf.msfconnect()

        # Modules
        self.axis = services.Axis(self)
        self.caidao = services.Caidao(self)
        self.elastic = services.Elastic(self)
        self.glassfish = services.GlassFish(self)
        self.iis = services.IIS(self)
        self.jenkins = services.Jenkins(self)
        self.jmx = services.JMX(self)
        self.mengine = services.ManageEngine(self)
        self.mysql = services.MySQL(self)
        self.phpmyadmin = services.PHPMyAdmin(self)
        self.psexec = services.PSExec(self)
        self.rdp = services.RDP(self)
        self.rubyonrails = services.RubyonRails(self)
        self.snmp = services.SNMP(self)
        self.ssh = services.SSH(self)
        self.struts = services.Struts(self)
        self.tomcat = services.Tomcat(self)
        self.unreal = services.Unreal(self)
        self.webdav = services.WebDAV(self)
        self.winrm = services.WinRM(self)
        self.wordpress = services.WordPress(self)

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
