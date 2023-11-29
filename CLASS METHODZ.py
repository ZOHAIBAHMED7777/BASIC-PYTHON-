 class Employee:
    
    bonus1 = 1000
    
    def Display(self):
        
        print('this is the parent class')
        
 class Manager(Employee):
     
     bonus2 = 2000
     
     def Show(self):
         
         print('this is the child class')
         
e1 = Employee()

m1 = Manager()

print(e1.bonus1)

print(m1.bonus2)

print(m1.bonus1)

print(e1.bonus2) #error they cannot access parent class 
        