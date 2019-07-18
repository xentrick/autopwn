#!/usr/bin/env python

from . import services
from . import util

import logging
<<<<<<< HEAD

log = logging.getLogger(__name__)
=======
log = logging.getLogger("autopwn")
>>>>>>> d537f072b49c577d17e2f458ecdbf666d7a28a11


class Autopwn(object):
    def __init__(self):
        log.info("Starting Autopwn!")
        return

    def scoreHost(self, host):
        log.info("Checking {}".format(host))

        # Verify address
        if not util.valid_ipv4(host):
            log.info("Invalid IPv4 address. Checking IPv6")
            if not util.valid_ipv6(host):
                log.info("Invalid address.")
                return -1
        log.info("Valid host address!")

        return 0

    def checkAll(self):
        log.info("Powering up the lasers. Preparing for world domination!")
        return
