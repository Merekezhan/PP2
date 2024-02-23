"""6 - Write a Python program to replace all occurrences of space, comma, or dot with a colon."""
import re

file=open("row.txt", "r", encoding="utf8")
text= file.read()

x = re.sub('[,.\s]',':', text)
print(x)

    