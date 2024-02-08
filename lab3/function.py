#task1
def calculate_factorial(n):
    if n == 1:
        return 1
    return calculate_factorial(n - 1) * n

# task2
def string_reverse(s):
    return s[::-1]

# task3
def maxx(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c

# task 4
def even_odd(a):
    if a % 2 ==0:
        return True
    else : 
        return False
#  task5
def isPrime(n):
    if n == 1:
        return True
    for i in range(2, round(n ** 0.5)+1):
        if n % i ==0:
            return False
    return True

def get_prime(listt):
    list2=[]
    for element in listt:
        if isPrime(element):
            list2.append(element)
    return list2

# a=[int(i) for i in input().split()]
# print(get_prime(a))

# task6
def find_common_elements(a, b):
    c=[]
    for elem in a:
        if elem in b:
            c.append(elem)
    return c

# task7
def word_frequency(a):
    d={}
    for word in a:
        if word in d:
            d[word]+=1
        else:
            d[word] = 1

# a=[word for word in input().split()]
# print(word_frequency(a))

# task8
def fibonnacci(n):
    if n == 1 :
        return 1
    if n == 2:
        return 1

    return fibonnacci(n - 1) + fibonnacci(n - 2)
# print (fibonnacci(6))

# task9
def calculate_running_average(a):
    l=[a[0]]
    for i in range (1, len(a)):
        l.append((l[i-1]*i + a[i])/(i + 1))
    return l
# a= [int(i) for i in input().split()]
# print(calculate_running_average(a))

    

    