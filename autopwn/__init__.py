#!/usr/bin/env python3

import sys
import logging

from . import services
from .autopwn import Autopwn

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("autopwn")
log.addHandler(logging.NullHandler())


def _real_main():
    Autopwn()
    sys.exit(0)


def main():
    _real_main()


__all__ = [n for n in globals().keys() if n[:1] != "_"]
