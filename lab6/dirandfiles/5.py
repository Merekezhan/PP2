import os
a = [i for i in input().split()]
f = open("C:\\Users\\admin\\Desktop\\pp2\\lab6\\dirandfiles\\demo5.txt", "w")
for elem in a:
    f.write(elem + " ")
f.close()