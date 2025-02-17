#!/usr/bin/env python3

import argparse
from smb.SMBConnection import SMBConnection
from smb.base import SMBTimeout, NotReadyError, NotConnectedError
from smb.smb_structs import UnsupportedFeature, ProtocolError, OperationFailure

import logging

log = logging.getLogger(__name__)


class Samba:
    def __init__(self):
        self.__smb = None
        self.__host = None
        self.__port = 445
        self.__user = "chewbacca"
        self.__pass = "rwaaaaawr5"
        self.__guest = "Guest"
        self.__guestpass = ""
        self.__domain = "WORKGROUP"
        self.__system = "*SMBSERVER"

    def __exploit(self):
        log.debug(f"[!] Attempting login to SMB ({self.__host})")
        self.__smb = SMBConnection(
            self.__user,
            self.__pass,
            # self.__guest,
            # self.__guestpass,
            self.__system,
            self.__host,
            self.__domain,
            use_ntlm_v2=True,
            sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
            is_direct_tcp=True,
        )
        try:
            if self.__smb.connect(self.__host, self.__port):
                print(self.__smb.listShares())
                log.info(f"[!] SMB is vulnerable ({self.__host})")
                return True
            else:
                log.info(f"[!] SMB is secure. Expected error. ({self.__host})")
                return False
        except ConnectionRefusedError as e:
            log.info(
                f"[!] SMB Connection refused. Get your server up you nut sack ({self.__host})"
            )
            log.debug(f"[+] Exception: {e}")
            return True
        except OperationFailure as e:
            log.info(f"[!] SMB is secure! Operation Failure. ({self.__host})")
            log.debug(f"[+] Exception: {e}")
            return False

    def servicebot(self):
        self.__smb = SMBConnection(
            "droid",
            "talos_is_known_to_rox",
            self.__system,
            self.__host,
            self.__domain,
            use_ntlm_v2=True,
            sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
            is_direct_tcp=True,
        )
        if self.__smb.connect(self.__host, self.__port):
            return True
        return False

    def run(self, host, user=None, pwd=None):
        self.__host = host
        log.debug(f"[+] Exploiting SMB ({self.__host})")
        if user:
            self.__user = user
        if pwd:
            self.__pass = pwd
        return self.__exploit()


def main(args):
    log.info("[+] SMB Enum by xentrick")
    log.info(f"[+] Exploiting {args.host}:{args.port}")

    exploit = Samba()
    if exploit.run(args.host, args.username, args.pwd):
        log.info("Target exploited")
    else:
        log.info("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("username")
    parser.add_argument("password")
    args = parser.parse_args()

    main(args)
