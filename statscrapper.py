#!/usr/bin/env python3
#
# FILE: statscrapper.py
# AUTHOR: Miguel Salvá
# ABSTRACT: This script scraps the content from a given URL (passed as an argument) and counts different status
#           icon to retrieve some stats. It can also login into a Confluence site 
#
# This script requires the beautifulsoup4, requests and atlassian-python-api libraries to run

import sys
import requests 
from bs4 import BeautifulSoup
from atlassian import Confluence

URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]

# Connects to the Confluence site
confluence = Confluence(url=URL, username=USERNAME, password=PASSWORD)
# confluence.page_exists(space, title)

req = requests.get(URL)
status_code = req.status_code
html_text = req.text
print(html_text)


