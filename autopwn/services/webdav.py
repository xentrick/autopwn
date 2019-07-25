

from .base import Service

import logging

log = logging.getLogger(__name__)


class WebDAV(Service):
    def __init__(self, autopwn):

        super(WebDAV, self).__init__()
        self._autopwn = autopwn
        self._msfrpcd = self._autopwn._msfrpcd

        self.name = "WebDAV"
        self.protocols = ["HTTP"]
        self.ports = [8585]
        self.exploits = ["auxiliary/scanner/http/http_put"]
        self.creds = {}
        self.cves = []
