# used to access methode of parents class


class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        return ("Car started")
    @staticmethod
    def stop():
        return ("car stopped")

class Toyotacar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)


c=Toyotacar("supra","electric")
print(c.type)
print(c.start())
print(c.stop())