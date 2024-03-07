"""Write a Python program with builtin function that returns True if all elements of the tuple are true."""
a = [eval(s) for s in input().split()]
b = tuple(a)
print(all(a))