import queue  
 
class queue_class:
    
    def __init__(self,items,num):
        if num == '1':
            self.list_items = items
            self.list_container = queue.Queue()
            self.massage = 'FIFO'
        elif num == '2':
            self.list_items = items
            self.list_container = queue.LifoQueue()
            self.massage = 'FILO'
    def list_append(self,add):
        self.add = add
        self.list_container.put(add)
        print()
        print(f'your value is add to queue ({self.massage}) : {add}')
    def list_pop(self):
        if self.list_container.empty():
            print()
            print(f'there is no items in queue ({self.massage}) you can add items by  pressing 1')
        else:
            print()
            rem =self.list_container.get()
            print(f'your value is removed from the queue ({self.massage}) :  {rem}')
        
    def container_print(self):
        if self.list_container.empty():
            print()
            print(f"there is no value in queue ({self.massage}) {self.list_items} you can chosse again ")
        else :
            print()
            print(f'the name of queue ({self.massage}) : {self.list_items} = {[i for i in self.list_container.queue]}')
 


if __name__=="__main__":
    main()





num = str(input("""Enter 1 want to work on FIFI
Enter 2 want to work on FIFO
"""))
if num == '1'or num == '2':
    
    name  = str(input("Enter the name of queue : "))
    name=queue_class(name,num)
else:
    print("you enter invalid option ! please run again ")
    exit()
 
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
        print("enter invalued value try again ")
        False
               
 
        
    

    
    
