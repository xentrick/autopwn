#!/usr/bin/env python3

import socket

import logging
log = logging.getLogger(__name__)


def checkIP(addr):
    log.debug("Checking {}".format(addr))

    # Verify address
    if not valid_ipv4(addr):
        log.info("Invalid IPv4 address. Checking IPv6")
        if not valid_ipv6(addr):
            log.info("Invalid address.")
            return False
    log.debug("Valid host address!")


def valid_ipv4(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(addr)
        except socket.error:
            return False
        return addr.count(".") == 3
    except socket.error:  # not a valid address
        return False

    return True


def valid_ipv6(addr):
    try:
        socket.inet_pton(socket.AF_INET6, addr)
    except socket.error:  # not a valid address
        return False
    return True
