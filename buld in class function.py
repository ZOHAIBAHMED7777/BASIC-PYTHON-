class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def change(self):
        self.name=input("enter the name ")
        self.age=input("enter the age")

e1=student('zohaib ahmed',20)
e2=student('muneeb khan',18)
print(e1.__dict__)
e1.change()
print(e1.__dict__)