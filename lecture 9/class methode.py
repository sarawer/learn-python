# a class methode is bound to the class and receives the class as an implicit first argument.

class person:
    name="anonymous"

    # def changeName(self,name):
    #     self.__class__.name=name

    @classmethod
    def changeName(cls,name):
        cls.name=name

p=person()
print(p.name)
p.changeName("sarawer")
print(p.name)
