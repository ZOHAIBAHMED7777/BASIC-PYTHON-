class Student:
    
    School_name = 'university of engineering and tecnology peshawar'
    
    def __init__(self, name , age):
        
        self.name = name
        
        self.age = age
        
    @classmethod
        
    def class_method(cls):
        
       print(f'the university name is :{ cls.School_name.upper()}')
        
student1 = Student('ZOHAIB AHMED',20)

student2 = Student('MUNEEB KHAN',18)

print(student1.__dict__)

print(Student.School_name)

print(student2.__dict__)

print(student1.School_name)

Student.class_method()





        