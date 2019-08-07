#!/usr/bin/env python3

import configparser
import os
import sys
from ctfdclient import CTFd
from pprint import pprint

import logging

log = logging.getLogger(__name__)


class Scoring(object):
    def __init__(self, ini="../config/challenges.ini"):
        log.info("[+] Initializing CTFD module")
        self.__moduledir = os.path.dirname(sys.modules[__name__].__file__)
        self.__ini = os.path.join(self.__moduledir, ini)
        self.config = configparser.ConfigParser()
        self.config._interpolation = configparser.ExtendedInterpolation()
        self.config.read(self.__ini)
        for i in self.config.sections():
            log.debug(f"Section: {i}")
            # for k, v in self.config.get(i):
            #     log.debug(f"Key: {k} Value: {v}")
        # pprint(self.config.options())

        self._addr = None
        self._port = None
        self.challenges = {}
        self._parse()

        self.ctfd = CTFd(
            f"http://{self._addr}:{self._port}", self._user, self._password
        )

    def _confExists(self, ini):
        log.debug(f"[+] Checking File: {ini}")
        try:
            os.path.isfile(ini)
        except Exception as e:
            log.debug(f"[!] Error: {e}")
            raise Exception("Error reading challenge configuration file")

    def _parse(self):
        if not self.config:
            raise Exception("Parsed configuration not available.")

        # print(self.ConfigSectionMap("scoreboard"))
        log.debug("Entries: {}".format(self.config))
        self._addr = self.config.get("Scoreboard", "host")
        self._port = self.config.get("Scoreboard", "port")
        self._user = self.config.get("Scoreboard", "user")
        self._password = self.config.get("Scoreboard", "password")
        log.debug(f"Scoreboard: http://{self._addr}:{self._port}")
        log.debug(f"Username: {self._user}")
        log.debug(f"Password: {self._password}")
        self._parseSections()

    def _parseSections(self):
        for s in self.config.sections():
            if s != "Scoreboard":
                self.challenges[s] = self.config.items(s)
        log.debug(f"Challenges: {self.challenges}")

    def award(self, team, chall):
        log.info(f"[+] Awarding {team} for {chall}")
        teamId = 1  # Temp value that doesn't seem to matter
        playerId = None  # Important value
        result = False
        if not self.challenges[chall]:
            return False
        challId = self.challenges[chall][1][1]
        log.debug(f"[!] Challenge: {chall} ID: {challId}")
        self.ctfd.players.update()
        for p in self.ctfd.players:
            if p.name.lower() == team.lower():
                playerId = p.id
                log.debug(f"[-] TeamID: {teamId}")
                result = self.ctfd.submissions.give(playerId, teamId, challId)
                if result:
                    log.info(f"[!] Awarded {team} points for {chall}")
                else:
                    log.info(f"[!] Failure to award points to {team} for {chall}")

    def ConfigSectionMap(self, section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
