import os, string
if not os.path.exists("letters"):
    os.makedirs("C:\\Users\\admin\\Desktop\\pp2\\lab6\\dirandfiles\\letters")
for letter in string.ascii_uppercase:
    with open("C:\\Users\\admin\\Desktop\\pp2\\lab6\\dirandfiles\\letters\\" + letter + ".txt", "w") as f:
        f.writelines(letter)