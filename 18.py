class account:
    def __init__(self, balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def cradit(self,amount):
        self.balance+=amount
        print(f"Rs  {amount} was cradit   ")
    def debit(self, amount):
        self.balance-=amount
        print(f"Rs {amount} was debit   ")
    def det_balance(self):
        print(f"the total balance is {self.balance}")

acc1=account(10000,376732764273)
acc1.debit(int(input("enter your amount you want to depit  ")))
acc1.cradit(int(input("enter your amount you want to credit ")))
acc1.det_balance()
