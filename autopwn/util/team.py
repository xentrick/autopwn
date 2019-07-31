#!/usr/bin/env python3

import requests

import logging

log = logging.getLogger(__name__)


def eligible(IP):
    try:
        log.debug(f"Retrieving team name for {IP}")
        r = requests.get(f"http://{IP}/team.txt")
        if r.status_code == 200:
            name = r.text.rstrip()
            log.debug(f"Team Name: {name}")
            return name
        log.debug(f"Finished {IP}")
    except Exception as e:
        log.debug(f"Exception: {e}")
        return None
