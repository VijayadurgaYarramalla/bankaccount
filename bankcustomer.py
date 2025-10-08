class SavingAccount:
    def __init__(self,account_holder,balance,pin,dailylimit):
       self.account_holder=account_holder
       self.balance=balance
       self.pin=pin
       self.dailylimit=dailylimit
       self.isactive=True
       self.atm_request=False
    def check_balance(self,pin):
        if not self.isactive:
            print("account not active")
        elif pin!=self.pin:
            print("invalid pin")
        else:
            print(f"current balance:{self.balance}")
    def withdraw(self,amount,pin):
        if not self.isactive:
            print("account not active")
        elif pin!=self.pin:
            print("invalid pin")
        elif amount>self.balance:
            print("amount not found")
        elif amount>self.daily_limit:
            print(f"amount exceed daily{self.dailylimit}")
        else:
            self.balance-=amount
            print(f"{amount} withdraw successfully and new balance {self.balnce}")
class BusinessAccount:
    def _init_(self,business_name,balance):
        self.business_name=business_name
        self.balance=balance
        self.isactive=True
    def check_balance(self):
        if self.isbalance:
            print("business balance:{self.balance}")
        else:
            print("account not active")
    def deposite(self,amount,pin):
        if pin!=self.pin:
            print("invalid pin")
        elif amount<=0:
            print("invalid amount")
        else:
            self.balance+=amount
            print("amount diposited successfully")
    

