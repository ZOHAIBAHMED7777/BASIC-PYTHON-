class employee():
    bonus=3000
    def dispaly(self):
        print('this is the empolyee class')
class manager(employee):
    bonus1=4000
    def show(self):
        print('this is the manager class')
e1=employee()
m1=manager()
e1.dispaly()
m1.show()
