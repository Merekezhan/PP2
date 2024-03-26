from time import sleep
import math

def sq(num, m):
    sleep(m/1000)
    x = math.sqrt(num)
    print(x)

num = int(input())
m = int(input())
sq(num, m)