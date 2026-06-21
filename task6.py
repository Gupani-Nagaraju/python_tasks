class Account:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Amount added successfully")
    
    def withdrawal(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount debeted successfully")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(self.__balance) 
    
class Savings_account(Account):
    pass

acc = Savings_account("Ramesh",123,1000)
acc.deposite(500)
acc.withdrawal(1000)
acc.show_balance()
acc.deposite(500)
acc.show_balance()