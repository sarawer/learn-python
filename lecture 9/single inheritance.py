# when Child class reuses parent class properties
class car:
    @staticmethod
    def start():
        return ("Car started")
    @staticmethod
    def stop():
        return ("car stopped")

class Toyotacar(car):
    def __init__(self,name):
        self.name=name

c=Toyotacar("supra")
print(c.start())
print(c.stop())