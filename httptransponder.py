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

def set_color(sc):
    """Function that gets an status code and returns a color"""
    if sc in range(100,199):    # 1xx Informational response
        return "\033[1;30;47m"
    elif sc in range(200,299):  # 2xx Success
        return "\033[1;37;42m"
    elif sc in range(300,399):  # 3xx Redirection
        return "\033[1;37;43m"
    elif sc in range(400,499):  # 4xx Client errors
        return "\033[1;37;41m"
    elif sc in range(500,599):  # 5xx Server errors
        return "\033[1;37;41m"
    else:
        return ""


# Main
OLD_STATUS_CODE = get_status_code(ENDPOINT)

while True: 
    NEW_STATUS_CODE = get_status_code(ENDPOINT)
    COLOR = set_color(NEW_STATUS_CODE)
    print(str(COLOR) + "HTTP status code: " + str(NEW_STATUS_CODE) + " | Current HTTP downtime: " + str(DOWNTIME) + " seconds                               ")
    time.sleep(1)
    if OLD_STATUS_CODE != NEW_STATUS_CODE:
        OLD_STATUS_CODE = NEW_STATUS_CODE
        DOWNTIME = DOWNTIME + 1
        break  # First HTTP status code change

while True:
    NEW_STATUS_CODE = get_status_code(ENDPOINT)
    COLOR = set_color(NEW_STATUS_CODE)
    print(str(COLOR) + "HTTP status code: " + str(NEW_STATUS_CODE) + " | Current HTTP downtime: " + str(DOWNTIME) + " seconds                               ")
    time.sleep(1)
    if OLD_STATUS_CODE != NEW_STATUS_CODE:
        break  # Second HTTP status code change
    else:
        DOWNTIME = DOWNTIME + 1

print ("")
print("Total HTTP downtime: " + str(DOWNTIME) + " seconds")

