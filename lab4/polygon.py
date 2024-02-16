import math 

def area_of_polygon(perimeter, apothem):
    area=0.5* perimeter* apothem
    return area

def perimeter(number_of_sides, length_of_side):
    perimeter=number_of_sides*length_of_side
    return perimeter

def apothem(number_of_sides, length_of_side):
    apothem= length_of_side/(2*math.tan(math.pi/number_of_sides))
    return apothem


number_of_sides=int(input())
length_of_side=int(input())

perimeter = perimeter(number_of_sides, length_of_side)
apothem = apothem(number_of_sides, length_of_side)
area=area_of_polygon(perimeter, apothem)

print("The area of regular polygon: " , area)



