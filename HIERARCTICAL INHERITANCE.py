class node:
    
    def __init__(self,data):
        
        self.data = data
        
        self.next = None
    
class link_list:
    
    def __init__(self):
        
        self.head = None

node1 = node(10)

node2 = node(20)

node3 = node(40)

node1.next = node2

node2.next = node3

print(node1.data,node1.next)

print(node2.data,node2)

print(node3.data,node3)
        