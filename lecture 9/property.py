# we use @property decorator on any method in the class to use the method as property.

class student:
    def __init__(self,math,phy,chem,bio):
        self.math=math
        self.phy=phy
        self.chem=chem
        self.bio=bio

    @property
    def calcAvg(self):
        return (self.math+self.phy+self.chem+self.bio)/4

s1=student(60,90,65,78)
print(s1.calcAvg)
s1.bio=99
print(s1.calcAvg)