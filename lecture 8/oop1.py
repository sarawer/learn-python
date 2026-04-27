# class is a blueprint for creating objects

# creating class
class Student:

    uni_name="SEU" #class attribute(Shared by all objects)

    def __init__(self,name,id):
        #This is a constructor (special function).
        # It runs automatically when we create an object.
        self.id=id  #object/instance attribute
        self.name=name  #object/instance attribute

    # methode(A function inside a class.Works with object data).always pass "self" parameter
    def welcome(self):
        print("welcome",self.name)

    # static method (Does NOT use self).It’s just a normal function inside a class (for organization)
    @staticmethod
    def msg():
        print("object created successfully")


s1=Student("sarawer",528)
Student.msg()
print(s1.uni_name,s1.name,s1.id)
s1.welcome()

s2=Student("rahat",527)
Student.msg()
print(s2.uni_name,s2.name,s2.id)
s2.welcome()
