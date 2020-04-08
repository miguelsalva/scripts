#!/usr/bin/env python3
#
# FILE: httptransponder.py
# AUTHOR: Miguel Salvá
# ABSTRACT: This script monitors HTTP status code changes for a given endpoint (passed as an argument)
#
# This script requires the requests library to run

import sys
import time
import requests

ENDPOINT = sys.argv[1]
DOWNTIME = 0
TERM_COLOR = "\033[1;37;40m"  # White text over black background

code_message = {
        100: 'Continue                           ', 101: 'Switching Protocols                ', 
        102: 'Processing                         ', 103: 'Early Hints                        ', 
        200: 'OK                                 ', 201: 'Created                            ', 
        202: 'Accepted                           ', 203: 'Non-Authoritative Information      ', 
        204: 'No Content                         ', 205: 'Reset Content                      ', 
        206: 'Partial Content                    ', 207: 'Multi-Status                       ', 
        208: 'Already Reported                   ', 226: 'IM Used                            ',
        300: 'Multiple Choices                   ', 301: 'Moved Permanently                  ', 
        302: 'Found                              ', 303: 'See Other                          ', 
        304: 'Not Modified                       ', 305: 'Use Proxy                          ', 
        306: 'Switch Proxy                       ', 307: 'Temporary Redirect                 ', 
        308: 'Permanent Redirect                 ', 400: 'Bad Request                        ', 
        401: 'Unauthorized                       ', 402: 'Payment Required                   ', 
        403: 'Forbidden                          ', 404: 'Not Found                          ',
        405: 'Method Not Allowed                 ', 406: 'Not Acceptable                     ', 
        407: 'Proxy Authentication Required      ', 408: 'Request Timeout                    ',
        409: 'Conflict                           ', 410: 'Gone                               ', 
        411: 'Length Required                    ', 412: 'Precondition Failed                ', 
        413: 'Payload Too Large                  ', 414: 'URI Too Long                       ', 
        415: 'Unsupported Media Type             ', 416: 'Range Not Satisfiable              ', 
        417: 'Expectation Failed                 ', 418: 'Im a teapot                        ', 
        421: 'Misdirected Request                ', 422: 'Unprocessable Entity               ', 
        423: 'Locked                             ', 424: 'Failed Dependency                  ', 
        425: 'Too Early                          ', 426: 'Upgrade Required                   ', 
        428: 'Precondition Required              ', 429: 'Too Many Requests                  ', 
        431: 'Request Header Fields Too Large    ', 451: 'Unavailable For Legal Reasons      ',
        500: 'Internal Server Error              ', 501: 'Not Implemented                    ', 
        502: 'Bad Gateway                        ', 503: 'Service Unavailable                ',
        504: 'Gateway Timeout                    ', 505: 'HTTP Version Not Supported         ', 
        506: 'Variant Also Negotiates            ', 507: 'Insufficient Storage               ', 
        508: 'Loop Detected                      ', 510: 'Not Extended                       ', 
        511: 'Network Authentication Required    '}

def get_status_code(ep):
    """Function that gets an endpoint and returns its HTTP status code"""
    req = requests.get(ep)
    return req.status_code

def set_color(sc):
    """Function that gets an status code and returns a color"""
    if sc in range(100,199):    # 1xx Informational response 
        return "\033[1;30;47m"  # Black text over white background
    elif sc in range(200,299):  # 2xx Success
        return "\033[1;37;42m"  # White text over green background
    elif sc in range(300,399):  # 3xx Redirection
        return "\033[1;37;43m"  # White text over yellow background
    elif sc in range(400,499):  # 4xx Client errors
        return "\033[1;37;41m"  # White text over red background
    elif sc in range(500,599):  # 5xx Server errors
        return "\033[1;37;41m"  # White text over red background
    else:
        return TERM_COLOR

def get_time():
    """Function that returns the current time formatted in a readable way"""
    return time.asctime(time.localtime(time.time()))


# Main
print("")
print("= httptransponder - HTTP status code for " + ENDPOINT)
print("= Stop the execution of the script with Ctrl-c")
print("")
OLD_STATUS_CODE = get_status_code(ENDPOINT)

while True: 
    try:
        NEW_STATUS_CODE = get_status_code(ENDPOINT)
        COLOR = set_color(NEW_STATUS_CODE)
        if NEW_STATUS_CODE in range(400,599):
            DOWNTIME = DOWNTIME + 1
        CURRENT_TIME = get_time()
        print(str(COLOR) + "HTTP status code " + str(NEW_STATUS_CODE) + ": " + code_message[NEW_STATUS_CODE] + " |   Current time: " + str(CURRENT_TIME) + "   " + TERM_COLOR)
        time.sleep(1)
    except KeyboardInterrupt:
        break

print("")
print("")
print("Total HTTP downtime: " + str(DOWNTIME) + " seconds")

