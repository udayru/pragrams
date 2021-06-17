import copy
import time
from functools import reduce
import random
l =[random.randint(1,100) for i in range(100)]
#l=[5,8,9,15,6]
import time
def outer(fun):
    def inner(x):
        start = time.time()
        print(fun(x))
        end = time.time()
        print(f'the time taken {end - start} function name {fun.__name__}')
    return inner
@outer
def list_items(items):
    items = copy.deepcopy(items)
    sorted_list=[]
    while items:
        temp = items[0]
        for i in items:
            if temp < i:
                temp = i
        sorted_list.append(temp)
        items.remove(temp)
    return sorted_list


@outer
def list_items_reduce(x):
    items = copy.deepcopy(x)
    sorted_reduce=[]
    while x:
        s =reduce(lambda z,y: z if z > y else y,x)
        x.remove(s)
        sorted_reduce.append(s)
    return sorted_reduce



list_items(l)
list_items_reduce(l)



    
    
    
        