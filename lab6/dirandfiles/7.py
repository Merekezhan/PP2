import os
first = open("C:\\Users\\admin\\Desktop\\pp2\\lab6\\dirandfiles\\demo.txt", "r")
second = open("C:\\Users\\admin\\Desktop\\pp2\\lab6\\dirandfiles\\demo22.txt", "a")
for lines in first:
    second.write(lines)


