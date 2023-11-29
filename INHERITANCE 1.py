class Computer_1:
    
    def __init__(self,ram,stor):
        
        self.ram = ram
        
        self.storage = stor
        
        print('computer_1 class ')

class Computer_2(Computer_1) :
    
    def __init__(self,ram,stor):
        
        super().__init__(ram,stor)
        
        self.processer = 'DDR DRIGEN '
        
        print(' computer_2 class')


comp_2 = Computer_2('8gb','512gb')

print(comp_2.__dict__)

        
        