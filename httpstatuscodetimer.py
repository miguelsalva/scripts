#!/usr/bin/env python3
#
# FILE: httpstatuscodetimer.py
# AUTHOR: Miguel Salvá
# ABSTRACT: This script monitors HTTP status code changes for a given endpoint (passed as an argument)
#
# This script requires the requests library to run

import sys
import time
import requests

ENDPOINT = sys.argv[1]
DOWNTIME = 0


def get_status_code(ep):
    """Function that gets an endpoint and returns its HTTP status code"""
    req = requests.get(ep)
    return req.status_code


# Main
OLD_STATUS_CODE = get_status_code(ENDPOINT)

while True: 
    NEW_STATUS_CODE = get_status_code(ENDPOINT)
    print("HTTP status code: " + str(NEW_STATUS_CODE) + " | Current HTTP downtime: " + str(DOWNTIME) + " seconds")
    time.sleep(1)
    if OLD_STATUS_CODE != NEW_STATUS_CODE:
        OLD_STATUS_CODE = NEW_STATUS_CODE
        DOWNTIME = DOWNTIME + 1
        break  # First HTTP status code change

while True:
    NEW_STATUS_CODE = get_status_code(ENDPOINT)
    print("HTTP status code: " + str(NEW_STATUS_CODE) + " | Current HTTP downtime: " + str(DOWNTIME) + " seconds")
    time.sleep(1)
    if OLD_STATUS_CODE != NEW_STATUS_CODE:
        break  # Second HTTP status code change
    else:
        DOWNTIME = DOWNTIME + 1

print ("")
print("Total HTTP downtime: " + str(DOWNTIME) + " seconds")

