dic = {'{':'}','[':']','(':')'}
st="{[({})]{})}}"
s=[]
flag = False
for i in st:
    if i in dic:
        s.append(i)
    else:
        if len(s)>=1:
            if i == dic[s[-1]]:
                s.pop()
                flag = True
        else:
            flag = False
if flag == True and len(s) == 0:
    print("its balanced")
else:
    print("its unbalanced")

        