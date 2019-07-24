

from .base import Service

import logging

log = logging.getLogger(__name__)


class Tomcat(Service):
    def __init__(self):

        self.name = "Apache Tomcat 8"
        self.protocols = ["HTTP"]
        self.ports = [8282]
        self.exploits = [
            "auxiliary/scanner/http/tomcat_enum",
            "auxiliary/scanner/http/tomcat_mgr_login",
            "exploits/multi/http/tomcat_mgr_deploy",
            "exploits/multi/http/tomcat_mgr_upload",
        ]
        self.creds = {"sploit": "sploit"}
        self.cves = ["CVE-2009-3843", "CVE-2009-4189"]
        super().__init__()
