class Bank:
    def __init__(self,balance,name):
        self.balance=balance
        self.name=name
    def deposit(self,amount):
        self.amount=amount
        self.balance+=amount
    def withdraw(self,amount):
        self.amount=amount
        self.balance-=self.amount
    def check_balance(self):
       return self.balance
class User(Bank):

    pass
obj=User()
obj.deposit(500(10000,'archana'))
