#!/usr/bin/env python

import socket


def valid_ipv4(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count(".") == 3
    except socket.error:  # not a valid address
        return False

    return True


def valid_ipv6(addr):
    try:
        socket.inet_pton(socket.AF_INET6, addr)
    except socket.error:  # not a valid address
        return False
    return True
