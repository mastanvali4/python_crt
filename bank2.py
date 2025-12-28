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
class SavingsAccounts(Account):
    def __init__(self,interest):
        self.interest=interest
        super().__init__(1000,"acc1234")
    def interestrate(self):
        interest1=self.balance*(self.interest/100)
        self.balance+=interest1
        print(self.getbal())
acc1=SavingsAccounts(5)
acc1.credit(500)
acc1.interestrate()
