# import socket
# print(socket.gethostbyname(socket.gethostname()))
#solution1
string="hello world, i made a basson today"
a=[]
s = string.replace(',','').split()
for i in s:
    for j in i:
        if i.count(j) >1:
            a.append(i)
            break
print(a)
# solution 2
c = [i for i in s if len(i) != len(set(i))]
print(c)

c=[]
for i in s:
    b=""
    for j in i:
        if j not in b:
            b+=j
        else:
            c.append(i)
print(c)

            