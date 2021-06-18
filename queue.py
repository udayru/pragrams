import queue  
 
class queue_class:
    
    def __init__(self,items):
        self.list_items = items
        self.list_container = queue.Queue()   
    def list_append(self,add):
        self.add = add
        self.list_container.put(add)
        print(f'your value is add to queue : {add}')
    def list_pop(self):
        if self.list_container.empty():
            print(f'there is no items in queue you can items pressing 1')
        else:
            rem =self.list_container.get()
            print(f'your value is removed from the queue :  {rem}')
        
    def container_print(self):
        if self.list_container.empty():
            print(f"there is not value in queue {self.list_items}")
        else :
            print(f' name is {self.list_items} and  {[i for i in self.list_container.queue]}')
        
name  = str(input("Enter the name of queue : "))
name=queue_class(name)

 
while True:
    print("""
Enter 1 if you want to add items
Enter 2 if you want to delete items
Enter 3 if you want to see Queue
Emter 4 to Exit from queue
""")
    ch = str(input("enter the value above number to work : "))
    
    if ch == '1':
        a = str(input("Enter the value to add in queue : "))
        name.list_append(a)
        
    elif ch == '2':
        name.list_pop()
    elif ch == '3':
        name.container_print()
    elif ch == '4':
        print("your exited successfully ")
        exit()
    else:
        print("enter invalued value")
        continue
        
#     print("enter to q to exit and c to continue : ")
#     ch_1=''
#     while ch_1!= 'q' and ch_1 != 'c':
#         ch_1 = input()
#         if ch_1 =='q':
#             exit()
#         elif ch_1=='c':
#             continue
#             
 
        
    

    
    