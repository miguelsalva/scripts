#!/usr/bin/env python3
#
# FILE: wordchopper.py
# AUTHOR: Miguel Salvá
# ABSTRACT: This script reads the content from a given COLUMN in an excel file (passed as an argument),
#           points out the content with more than WORD_MAX_SIZE characters, separates the allowed content by 
#           a SEPARATOR and writes the output into a TXT_FILE. 
#
# This script requires the pandas library to run

import sys
import pandas

EXCEL_FILE = sys.argv[1]
TXT_FILE = "leavers.txt"
COLUMN = "Long ID/Number"
WORD_MAX_SIZE = 40
SEPARATOR = ","

df = pandas.read_excel(EXCEL_FILE)
content = ""

print("Please find below content with more than 40 characters:")
for i in range(len(df)):
    try:
        df.loc[COLUMN, i] = df[COLUMN][i].strip()
        if len(df[COLUMN][i]) > WORD_MAX_SIZE:
            print(df[COLUMN][i])
        else:
            content = content + df[COLUMN][i] + SEPARATOR
    except AttributeError:
        pass

print("")
content = content[:-1]

fip = open(TXT_FILE, "w")
fip.write(content)
fip.close()
