import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

x = re.findall("ai", txt)
print(x)

x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
txt = "The rain in Spain Sos"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())