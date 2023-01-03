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
s = myfilter(lambda x : x[0].isdigit() , strings)
print(s)

# 2-B
k = ['abcde', 'mynameis', 'character', 'cartoon', 'hi', 'human']
o = myfilter(lambda x : len(x) > 6, k)
print(o)

# 2-C
l = 'Hi my name is rachit i like dancing and coding it is the best thing to do in the morning !'
ok = myfilter(lambda x : 'ing' in x, l.split())
print(ok)
