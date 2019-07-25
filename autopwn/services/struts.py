

from .base import Service

import logging

log = logging.getLogger(__name__)


class Struts(Service):
    def __init__(self, autopwn):

        super(Struts, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "Apache Struts"
        self.protocols = ["HTTP"]
        self.ports = [8282]
        self.exploits = ["exploit/multi/http/struts_dmi_rest_exec"]
        self.creds = {"sploit": "sploit"}
        self.cves = ["CVE-2016-3087"]
