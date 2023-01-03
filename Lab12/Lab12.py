def mymap(func, iterable):
    a = []
    for i in iterable:
        x = func(i)
        a.append(x)
    return a

def myfilter(func, iterable):
    a = []
    for i in iterable:
        if func(i):
            a.append(i)
    return a

def myreduce(func,iterable):
    element = ''
    for i in iterable:
        element = func(element,i)
    return element

# 1-A
n = int(input('Enter a number: '))
z = mymap(lambda x : x**2, range(1,n+1,2))
print(z)

# 1-B
words = ['go', 'work', 'study', 'play']
a = mymap(lambda x : x + 'ing', words)
print(a)

# 1-C
x = mymap(lambda x : (x,len(x)), words)
print(x)  

# 2-A
strings = ['1sa', '3sjf', 'myname', 'wordas', 'jdi6bd']
s = myfilter(lambda x : not x[0].isdigit() , strings)
print(s)

# 2-B
k = ['abcde', 'mynameis', 'character', 'cartoon', 'hi', 'human']
o = myfilter(lambda x : len(x) > 6, k)
print(o)

# 2-C
l = input("Enter a line: ").split()
suffix = input("Enter a suffix: ")
ok = myfilter(lambda x : x.endswith(suffix), l)
print(ok)

# 3-A
name = input("Enter a name: ").split()
print(myreduce(lambda x,y: x + y[0], name))