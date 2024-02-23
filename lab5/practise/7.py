"""7 - Write a python program to convert snake case string to camel case string."""

import re

file=open("row.txt", "r", encoding="utf8")
text= file.read()

x =  re.split("_",text) 



    