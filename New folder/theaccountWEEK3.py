class BankAccount:
    rate_of_interest = 5
    min_balance = 100

    def __init__(self, account_no, owner_name, balance):
        self.account_no = account_no
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        # self.balance = self.balance - amount
        if (self.balance - amount) < BankAccount.min_balance:
            print("Cannot withdraw the money")
        else:
            self.balance = self.balance - amount
            print(self.balance)

    def deposit(self, amount):
        self.balance = (self.balance + amount) * (BankAccount.rate_of_interest / 100)
        print(self.balance)

    @staticmethod
    def variable_rate(x):
        return x+(BankAccount.rate_of_interest/100)+(BankAccount.min_balance/10)

print(BankAccount.variable_rate(1000))
a1 = BankAccount("000111", "Amandeep Kaur", 1000)
a2 = BankAccount("000222", "Ashish Kumar", 1500)
a1.withdraw(100)
# a2.deposit(100)


