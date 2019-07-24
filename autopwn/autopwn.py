#!/usr/bin/env python

from . import services
from . import util

import logging

log = logging.getLogger(__name__)
log = logging.getLogger("autopwn")


class Autopwn(object):
    def __init__(self):
        log.info("Starting Autopwn!")

        # Modules
        self.axis = services.Axis()
        self.caidao = services.Caidao()
        self.elastic = services.Elastic()
        self.glassfish = services.GlassFish()
        self.iis = services.IIS()
        self.jenkins = services.Jenkins()
        self.jmx = services.JMX()
        self.mengine = services.ManageEngine()
        self.mysql = services.MySQL()
        self.phpmyadmin = services.PHPMyAdmin()
        self.psexec = services.PSExec()
        self.rdp = services.RDP()
        self.rubyonrails = services.RubyonRails()
        self.snmp = services.SNMP()
        self.ssh = services.SSH()
        self.struts = services.Struts()
        self.tomcat = services.Tomcat()
        self.webdav = services.WebDAV()
        self.winrm = services.WinRM()
        self.wordpress = services.WordPress()

    def scoreHost(self, host):
        util.ip.checkIP(host)

    def checkAll(self):
        log.info("Powering up the lasers. Preparing for world domination!")
        return
