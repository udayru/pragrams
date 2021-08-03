import sys
import enum
class days(enum.Enum):
    sunday=0
    monday=1
    tuesday=2
    wednesday=3
    thusday=4
    friday=5
    saturday=6    
n= sys.argv[1].lower()
flag = True
for i in days:
    if n == i.name:
        print(i.value)
        flag = False
        break
if flag:
    print("enter properly")
print(sys.argv[2])