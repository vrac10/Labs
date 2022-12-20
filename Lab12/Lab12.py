"""
1. Write a Python program using lambda function
    a) To find a given sting starts with a given character
    b) To extract year, month, day from datetime
    c) To sort a list of distionaries based on a given key

2. Write a pyhton program using map/reduce/filter and lambda
    a) Given a list of strings, remove all strings having first character as digit
    b) Given a list of numbers, find maximum in the list
    c) Given a list of tuples containing two integers, remove all tuples where second elemnt in tuple is not a factor of first element

3. Write a function to mimic reduce called - myreduce . Test this with the following
    a) Given a list of numbers, find maximum in the list
    b) Given a list of integers, combine all integers to form a single intege

"""

# 1-A
a = lambda x,y : x[0] == y
word = input("Enter the word: ")
letter = input("Enter the letter to be checked: ")
print(a(word,letter))

# 1-B
import datetime
date = datetime.datetime.today().date()
day = lambda y : y.month
month = lambda z : z.day
year = lambda a : a.year
print(day(date),month(date),year(date))

# 2-A
a = ['8aabced', 'abcde', '1ade', 'abdbiad']
digitremove = list(filter(lambda x : x[0].isalpha(), a))
print(digitremove)

# 2-B
z = list(filter(lambda x : x % 2 == 0, range(1,20)))
a = lambda x : max(x)
print(a(z))
 
# 2-C
a = [(2,1),(5,2),(27,6),(69,13),(55,23),(24,12)]
x = list(filter(lambda x : True if x[0] % x[1] == 0 else False,a))
print(x)

# 3-A
def myreduce(func,iterable):
    element = iterable[0]
    for i in iterable:
        element = func(element,i)
    return element
a = myreduce(lambda x,y : x if x > y else y, [1,7,12,5,3,24])
print(a)

# 3-B
b = myreduce(lambda x,y : x+y, [1,7,12,5,3,24])
print(b)

    
    





