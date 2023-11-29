class Node:
    def __init__(self,data):
        
        self.data=data
        
        self.next=None
        
class Stack:
    
    def __init__(self):
        
        self.top=None 
        
    def push(self):
        
        x=int(input('enter the elements inserted in stack'))
        
        new=Node(x)
        
        if self.top is None:
            
            self.top=new
            
            self.top.next=None
            
        else:
            
            new.next=self.top
            
            self.top=new
            
    def pop(self):
        
        if self.top is None:
            
            print('stack is empty')
            
        elif self.top.next is None:
            
            print('popped elements is :',self.top.data)
            
            print('---------------------------------')
            
            self.top=None
        else:
            
            temp=self.top
            
            print('popped element is :',self.top.data)
            
            self.top=temp.next
            
            temp=None
            
    def display(self):
        
        if self.top is None:
            
            print('Empty stack')
            
            print('----------------')
            
        else:
            
            print('Elements of the stack are:')
            
            temp=self.top
            
            while temp:
                
                print(temp.data)
                
                temp=temp.next
                
            print('the top of the stack is ',self.top.data)
            
            print('--------------------------------------')
            
s=Stack()

while(1):
    
    print('enter the option from below')
    
    print('1_push opration')
    
    print('2_pop opration')
    
    print('3_display')
    
    print('n 4_exit')
    
    option=int(input('-------'))
    
    if option==1:
        
        print('push opration')
        
        print('--------------')
        
        s.push()
        
    elif option==2:
        
        print('pop opration')
        
        print('------------')
        
        s.pop()
        
    elif option==3:
        
        print('display')
        
        print('--------')
        
        s.display()
        
    else:
        
        break
    
        