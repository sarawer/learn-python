# Create A account class with 2 attributes -Balance and Account number. Create method for Debit , Credit and printing the balance

class account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
        print("account created successfully")

    def debit(self,amount):
        self.balance-=amount
        print("debit amount:",amount)

    def credit(self,amount):
        self.balance+=amount
        print("credit amount:",amount)

    def chk_balance(self):
        print("Balance:",self.balance)


a1=account(5000,111)
a1.debit(200)
a1.chk_balance()
a1.credit(3000)
a1.chk_balance()


