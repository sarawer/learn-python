#private attribute
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass   # this attribute is private attribute. object cant access it but class can.

a1=account(1111, 1234)

print(a1.acc_no)
print(a1.__acc_pass) #error