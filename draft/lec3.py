# ex1
# def greet(var1, var2):
#     print("Hello world", var1 , var2)
# greet("student","teacher")   

    # ex2
# def greet(var1, var2):
#     print("Hello world", var1 , var2)
#     return var1 +var2 
# response = greet(1,3)
# print (response)

    # ex3
# def greet(vars):
#     print("Hello world", vars)
#     return vars[3] 

    # ex4
# def greet(var1, var2):
#     print("your var2",  var2)
#     return var2 

# keyworded_func(3,6)


# def dynanic_func(**vars):
#     print(vars)
# dynamic_func(var3=2, var1=6)


    # ex5
# def keyworded_func(var1, var2, var3, var4): 
#     print("your var2:",var2)
#     return var2
 
# keyworded_func(2, 6, 8, 9)

    #  ex6
# def keyworded_func(var1, var2, var3):
#     print("Variants are:", var1,  var2, var3)
#     return var1, var2, var3
# keyworded_func(1, 2, 3)

#  ex7
# import math
# print(int(math.sqrt(4)))
# print(math.pow(2, 4))

#     ex8

# my_lambda=lambda x:x+1
# print(my_lambda(2))

# mylist=[1,2,3]
# for i in mylist:
#     print(my_lambda(i))

#  ex9
# def sum(a, b):
#     return (a+b)
# a= int(input("Enter 1st number"))
# b= int(input("Enter 2nd number"))

# print(f"sum of {a} and {b} is {sum(a, b)}")

# ex10
# class MyCycle():
#     def __init__(self, x, y) :
#         self.x=x
#         self.y=y
#         self.radius=5
#     def count_area(self):  
#         return 3.14 * self.radius * self.radius  
       
# myobject_point= MyCycle(1,2)      
# print(myobject_point.count_area())  


import math 

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self, newp):
        return math.sqrt((self.x - newp.x) ** 2 + (self.y - newp.y)**2)
    def q(self):
        self.shirek = 0

class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.rad = radius
    def set_center(self, newcenter):
        self.center.x = newcenter.x
        self.center.y = newcenter.y
    def set_rad(self, newrad):
        self.rad = newrad
        
    def area(self):
        self.area =  math.pi * self.rad ** 2
        return self.area
    
    def peri(self):
        return math.pi * 2 * self.rad
    
    def is_in(self, givpoint):
        distance = givpoint.dist(self.center)
        if distance > self.rad:
            return "ne lezhit vnutri"
        elif distance < self.rad:
            return "lezhit vnutri"
        else:
            return "lezhit na granice"


p1 = Point(0,4)
p2 = Point(7,8)
circ1 = Circle(p1, 3)
print(circ1.area())
print(circ1.peri())
print(circ1.is_in(p2))
p3 = Point(7,6)
circ1.set_center(p3)
print(circ1.is_in(p2))
circ1.set_rad(0.1)
print(circ1.is_in(p2))


class sportsman():
    def __init__(self, id , sport_name) :
        self.id= id
        self.sport_name= sport_name
    def set_id(self, new_id):
        self.id= new_id
    def set_namee(self, newname):
        self.namee = newname
        
    
class group(sportsman):
    def __init__ (self, id, sport_name, num_players):
        super().__init__(id,sport_name)
        self.num = num_players
class football(group):
    def __init__(self, id, sport_name, num_players, name):
        super().__init__(id, sport_name, num_players)
        self.name = name