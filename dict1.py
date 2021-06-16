l={'a':[3,4,5],'b':[5,7,2,3],'c':[9,5,4,3]}
d=[]
for i ,j in l.items():
    for k in j:
        d.append(i+str(k))
print(d)