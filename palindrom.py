text=input(str("enter the text : "))
text2 =''
for i in range(len(text)-1,-1,-1):
    text2+=text[i]
if text == text2:
    print("its a palindrom")
else:
    print("its not a palindrom")