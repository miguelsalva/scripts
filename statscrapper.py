#!/usr/bin/env python3
#
# FILE: statscrapper.py
# AUTHOR: Miguel Salvá
# ABSTRACT: This script reads the content from a given URL (passed as an argument) and counts different status
#           icon to retrieve some stats 
#
# This script requires the beautifulsoup4 and requests libraries to run

import sys
import requests 
from bs4 import BeautifulSoup
from atlassian import Confluence

URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]

confluence = Confluence(url=URL, username=USERNAME, password=PASSWORD)
# confluence.page_exists(space, title)

req = requests.get(URL)
status_code = req.status_code
html_text = req.text
print(html_text)


