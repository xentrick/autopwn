import argparse
import logging
from pprint import pprint
from autopwn import exceptions
from autopwn import Autopwn
import sys

logging.basicConfig(level=logging.DEBUG, format="%(levelname)5s %(module)10s:%(lineno)3s: %(message)s")
log = logging.getLogger("autopwn")

def main():
    parser = argparse.ArgumentParser(
        description="Autopwn - Automated Metasploit3 vuln tester",
    )

    parser.add_argument('target', help="Target IP")

    try:
        pwn = Autopwn()

        args = parser.parse_args()

        tar = args.target

        # MySQL
        pprint(pwn.mysql.msfcore())
        print(pwn.mysql.name)
        #pprint(pwn.mysql.search())
        pprint(pwn.mysql.search("mysql"))
        log.debug("Attempting score")
        pwn.scoreHost(tar)

    except exceptions.AutoPwnException as e:
        print(f"AutoPwn exception occured: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unhandled exception occured: {e}")
        sys.exit(1)

