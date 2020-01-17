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

ok_total = 0
wr_total = 0
ko_total = 0

# Connects to the Confluence site
confluence = Confluence(url=URL, username=USERNAME, password=PASSWORD)
# confluence.page_exists(space, title)

req = requests.get(URL)
#status_code = req.status_code
#html_text = req.text
html = BeautifulSoup(req.text, 'html.parser')

ok_entries = html.find_all('img',{'class' : 'emoticon-tick'})
wr_entries = html.find_all('img',{'class' : 'emoticon emoticon-warning'})
ko_entries = html.find_all('img',{'class' : 'emoticon emoticon-cross'})

print(ok_entries)
print(wr_entries)
print(ko_entries)
#print(html)
