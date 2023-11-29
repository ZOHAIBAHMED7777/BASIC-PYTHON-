class student:
    school_name='uet peshawar'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def get_school_name(cls):
        cls.school_name='university'
        print(f"the school name is",cls.school_name)
        
std1=student('zohaib ahmed',20)
std2=student('mueeb ahmed',19)

student.get_school_name()
print(std1.school_name)
