import math

def calculate_area_parallelogram(length, height):
    area = length * height
    return area

length=int(input())
height=int(input())

area = calculate_area_parallelogram(length, height)
print("The area of parallelogram is: ", area)