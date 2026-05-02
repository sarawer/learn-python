#private method
class person:
    def __init__(self,name):
        self.name=name
    def __hello(self):
        print("hello")
    def welcome(self):
        self.__hello() # it won't give error cz a private method can be used inside the class

p=person("arawer")
p.welcome()
p.__hello() #it will give error . cz __hello is a private method and object cant accesss it
