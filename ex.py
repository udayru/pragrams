import string
string = "hello world, i am naggappan"
string.replace(',','')
string.replace(' ','')

print(string)
"""d={}
for i in string:
    if i not in d:
        cont =0
        for j in string:
            if i == j:
                 cont= cont+1
        if i != ' ':
            d[i]=cont
print(d)
print(type(d))
c=0
v={}
for i,j in d.items():
    
    if j > c:
        v.clear()
        c=j
        v[i]=j
print(v)

"""
c={}
d={}
s=string.replace(' ','')
for i in s:
    t=0
    if i not in d:
        count =0
        for j in s:
            if j==i:
                count=count+1
        if i != ',':
            d[i]=count
                
            
print(d)
count=0
for i,j in d.items():
    
    if j > count:
        c.clear()
        count=j
        c[i]=j
print(c)   


    
        
    
