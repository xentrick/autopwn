#!/usr/bin/env python3

import argparse
import ipaddress
from autopwn import Autopwn
from pprint import pprint

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("autopwn")
paralog = logging.getLogger("paramiko").setLevel(logging.WARNING)
smblog = logging.getLogger("SMB").setLevel(logging.WARNING)
paralog = logging.getLogger("requests").setLevel(logging.WARNING)
paralog = logging.getLogger("urllib3").setLevel(logging.WARNING)
#ctfdlog = logging.getLogger("ctfdclient").setLevel(logging.DEBUG)


def verifyCIDR(block):
    return ipaddress.ip_network(block)

def verifyAddr(IP):
    return str(ipaddress.ip_address(IP))

def listIPs(block):
    return [str(ip) for ip in block.hosts()]


def main(args):
    if args.debug:
        log.setLevel(logging.DEBUG)
        pwn = Autopwn(debug=True)
    else:
        pwn = Autopwn()
    if args.host:
        pwn.checkAll([verifyAddr(args.host)])
    else:
        block = verifyCIDR(args.cidr)
        pwn.checkAll(listIPs(block))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cidr")
    parser.add_argument("--host", action="store", dest="host", required=False)
    parser.add_argument(
        "-d", "--debug", action="store_true", dest="debug", required=False
    )
    args = parser.parse_args()

    main(args)
