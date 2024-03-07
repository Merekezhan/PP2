import os
print("Test a path exists or not:")
path = r'demoo.txt'
print(os.path.exists(path))
path = r'C:\\Users\\admin\\Desktop\\pp2\\lab6\\dirandfiles\\3.py'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))