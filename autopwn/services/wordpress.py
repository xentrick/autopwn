

from .base import Service

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class WordPress(Service):
    def __init__(self, autopwn):

        super(WordPress, self).__init__(autopwn)

        self.name = "WordPress"
        self.protocols = ["HTTP"]
        self.ports = [8585]
        self.exploits = ["unix/webapp/wp_ninja_forms_unauthenticated_file_upload"]
        self.creds = {}
        self.cves = ["CVE-2016-1209"]
