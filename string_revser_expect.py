a='uday is good person'
b=''
c=a.split(' ')
for i in c:
    #print(i)
    b+=(f'{i[0].upper()}{i[1:][::-1]} ')
    #b+=(f'{i[0].upper()}{i[1:]} ')
    
    
    
print(b)
print(f'this capitalz is : {a.title()}')    