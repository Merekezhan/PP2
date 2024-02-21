"""1  Create a generator that generates the squares of numbers up to some number N."""
def squares_of_numbers(n):
    for i in range(n):
        yield i **2
num=int(input())
for x in squares_of_numbers(num):
    print(x)



"""2 - Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
"""
def even_numbers(n):
    for i in range(1, n):
        if i % 2==0:
            yield i
san= int(input())
for x in even_numbers(san):
    print(x)


"""3 - Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n."""
"I divided it by 12=(3*4)"

def divisible_by(n):
    for i in range(n):
        if i % 12==0:
            yield i
san=int(input())
for x in divisible_by(san):
    print(x)


"""4 - Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values."""

def squares(a, b ):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())
for x in squares(a,b):
    print(x)

"""5 - Implement a generator that returns all numbers from (n) down to 0."""

def number_down_zero(n):
    for i in range(n, 0, -1):
        yield i 
num = int(input())
for x in number_down_zero(num):
    print((x))
