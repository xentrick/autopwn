

from .base import Service

import logging

log = logging.getLogger(__name__)


class Jenkins(Service):
    def __init__(self, autopwn):

        super(Jenkins, self).__init__(autopwn)

        self.name = "Jenkins"
        self.protocols = ["HTTP"]
        self.ports = [8484]
        self.exploits = [
            "exploits/multi/http/jenkins_script_console",
            "auxiliary/scanner/http/jenkins_enum",
        ]
        self.creds = {}
