#!/usr/bin/env python3

from ..const import MSFUSER, MSFPASS, MSFSERVER, MSFPORT, MSFSSL

from pymetasploit3.msfrpc import MsfRpcClient

import logging

log = logging.getLogger(__name__)


def msfconnect():
    return MsfRpcClient(
        MSFPASS, username=MSFUSER, ssl=MSFSSL, server=MSFSERVER, port=MSFPORT
    )


def splitmodule(module):
    if not isinstance(module, str):
        raise TypeError("Module must be a string")
    """ Split module type and path """
    try:
        mType, mPath = module.split("/", 1)
    except ValueError as e:
        raise ValueError("Incorrect module format: {}".format(module))
    else:
        log.debug("Module Type: {}".format(mType))
        log.debug("Module Path: {}".format(mPath))
        return mType, mPath


def verifyJob(job):
    if not isinstance(job, dict):
        raise TypeError("Job must be in dictionary format")
    elif "job_id" not in job.keys():
        raise TypeError("Invalid job object")
    elif job["job_id"] is None:
        return False
    return True
