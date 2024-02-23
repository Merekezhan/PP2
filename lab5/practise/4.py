"""4 - Write a Python program to find the sequences of one upper case letter followed by lower case letters."""
import re

file=open("row.txt", "r", encoding="utf8")
text= file.read()

if re.findall('[A-Z][a-z]+', text):
    print("matches")
else:
    print("no matches")