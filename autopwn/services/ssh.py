#!/usr/bin/env python3

from .base import Service
from ..const import creds

import logging

log = logging.getLogger(__name__)


class SSH(Service):
    def __init__(self):

        self.name = "SSH"
        self.protocols = ["SSH"]
        self.ports = [22]
        self.exploits = [
            # Fix it
        ]
        self.creds = creds
        super().__init__()
