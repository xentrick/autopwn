

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class SSH(Service):
    def __init__(self, autopwn):

        super(SSH, self).__init__(autopwn)

        self.name = "SSH"
        self.protocols = ["SSH"]
        self.ports = [22]
        self.exploits = [
            # Fix it
        ]
        self.creds = creds
