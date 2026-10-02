class Account:
    account_number = "12345678"
    acc_name = "Bharat"
    balace = 40000

    def __init__(self, deposite, balance):
        self.deposite = deposite
        self.balance = balance

    def get_deposite(self):
        print(self.deposite)

    def checkbalance(self):
        print(self.balance)    
        

p1  = Account(60000, 40000)
p1.get_deposite()

p1.checkbalance()

