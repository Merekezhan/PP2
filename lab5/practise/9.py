"""9 - Write a Python program to insert spaces between words starting with capital letters."""
import re

file = open("row.txt", "r", encoding="utf8")
text = file.read()
x = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(x)