# when Child class reuses parent class properties
class car:
    milage=20
    @staticmethod
    def start():
        return ("Car started")
    @staticmethod
    def stop():
        return ("car stopped")

class Toyotacar(car):
    def __init__(self,brand):
        self.brand=brand

class supra(Toyotacar):
    def __init__(self,type):
        self.type=type

s=supra("diesel")
print(s.start())
print(s.stop())
print(s.milage)
# print(s.brand) # error