string = "python is the great python and java also great"
a= string.split(' ')
b=[]
for i in a:
    if i not in b:
        b.append(i)
        print(i,end=' ')
        