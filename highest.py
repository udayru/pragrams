l=[5,8,9,15,6]
t=[]
while l:
    m = l[0]
    for i in l:
        if m < i:
            m=i
    l.remove(m)
    t.append(m)
print(f'highest is {t[0]}, 2rd hightest is {t[1]}')        
    