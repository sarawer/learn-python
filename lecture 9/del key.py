#Del keyword
class student:
    def __init__(self,name):
        self.name=name


s1=student("sarawer")
print(s1.name)
del s1.name
print(s1.name)  # AttributeError: s1 object has no attribute 'name'.
# we can also delete an object or class by using del key.If we delete a class but an object already exists,
# that object still works — because the object holds its own reference:

