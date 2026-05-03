# define an employee class  with attributes role,department and salary.
# this class also has a showDetails() methode.
# create an engineer class that inherit properties from employee and has additional attributes name and age

class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("Role:",self.role)
        print("department:",self.dept)
        print("salary:",self.salary)

class engineer(employee):
    def __init__(self,name,age,role,dept,salary):
        self.name=name
        self.age=age
        super().__init__(role,dept,salary)


e1=engineer("Elon musk","23","Engineer","IT","100000")

e1.showDetails()