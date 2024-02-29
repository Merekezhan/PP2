"""7 - Write a python program to convert snake case string to camel case string."""


import re
a = re.split('_', input())
for elem in a:
    elem=elem.lower()
    print(elem.capitalize(), end="")



    