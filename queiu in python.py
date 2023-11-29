def enqueue():
    
    x = int(input('enter the queue elements which is inserted'))
    
    queue.append(x)
    
def delqueue():
    
    if len(queue)==0:
        
        print('empty queue')
        
        print('------------')
        
    else:
        
        print(queue[0],'is deleted from the queue')
        
        del queue[0]
        
        print('------------')
        
def display():
    
    if len(queue)==0:
        
        print('queue is empty')
        
    else:
        
        print('the elements of queue are:')
        
        for ele in queue:
            
            print(ele)
            
        print('front of the queue is :',queue[0])
        
        print('rair of the queue is :',queue[-1])
        
        print('--------------------------------')
        
        
queue=list()

while(1):
    
    print('1_stored queue')
    
    print('2_del queue')
    
    print('3_display')
    
    print('4_exit')
    
    option=int(input("----"))
    
    if option==1:
        
        print('queue stored opration')
        
        enqueue()
        
    elif option==2:
        
        print('delete queue opration ')
        
        delqueue()
        
    elif option==3:
        
        print('display queue value')
        
        display()
        
    else:
        
        break