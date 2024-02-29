"""10 - Write a Python program to convert a given camel case string to snake case."""

import re

a = re.findall('.[^A-Z]*', input())
str = ""
for elem in a:
    str += elem.lower() + "_"
print(str[:-1])