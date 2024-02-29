"""8 - Write a Python program to split a string at uppercase letters."""

import re

a = re.split('[A-Z]', input())
for elem in a:
    print(elem)
