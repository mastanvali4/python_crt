class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit (self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"{amount} is debited,bal is {self.getbal()}")
        else:
            print("insufficient funds")
    def credit (self,amount):
        self.balance+=amount
        print(f"{amount} is credit,bal is {self.getbal()}")
    def getbal(self):
        return self.balance
acc1=Account(1000,"acc1234")
acc1.credit(500)
acc1.debit(123)
