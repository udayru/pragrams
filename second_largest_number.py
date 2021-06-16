from functools import reduce
def second(a):
    s=a[0]
    for i in range(1,len(a)):
        if s < a[i]:
            s=a[i]
        else :
            pass
    return s
x=[51,2,3,41,6,42]
print(second(x))

for i in range(2):
    s =reduce(lambda i,y: i if i > y else y,x)
    x.remove(s)
    
print(s)