class Person:
    
    def __init__(self,name,age):
        
        self.name = name
        
        self.age = age 
        
class Employee(Person):
    
    def __init__(self,name,age):
        
        super(). __init__(name,age)

        self.salary = 50000
        
class Student(Employee):
    
    def __init__(self,name,age,marks):
        
        super(). __init__(name,age)
        
        self.marks = marks
        
p1 = Person('zohaib ahmed',20)

e1 = Employee('muneeb khan',18)

s1 = Student('maaz khan',15,92)

print(p1.__dict__)

print(e1.__dict__)

print(s1.__dict__)