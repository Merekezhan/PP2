# import math

# h=int(input("Input height: "))
# a=int(input("Input first value: "))
# b=int(input("Input second value: "))

# area=0.5*h*(a+b)

# print("The area of a trapezoid: ",area)

def calculate_area_trapezoid(height, base1, base2):
    area=0.5*height*(base1 + base2)
    return area

height=int(input())
base1=int(input())
base2=int(input())


area = calculate_area_trapezoid(height, base1, base2)
print("The area of a trapezoid: ", area)