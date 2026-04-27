# create a student class that takes name and marks of 3 students as arguments in constructor.Then creat a method to print the average

class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        summ=0
        for mark in self.marks:
            summ+=mark
        print("hi",self.name,"your average mark is:",summ/len(self.marks))


s1=student("sarawer",[90,80,85])
s1.avg()

s2=student("rahat",[90,95,80])
s2.avg()

s3=student("niloy",[90,95,100,78])
s3.avg()
