# Create Account class with 2 attributes - balance & account number.
# Create methods for debit , credit & printing the balance.

class Account:
    Account_Number = "Ansh7982779904"
    def __init__(self, balance):
        self.balance = balance
        print("Account Number:", (self.Account_Number) , "\nAvailable Balance:", (self.balance) , "Rupees")

    def debit(self, debit_amount):
        if debit_amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= debit_amount
            print("Debited Amount", (debit_amount), "Rupees", "\nRemaining Balance:", (self.balance), "Rupees")

    def credit(self, credit_amount):
        self.balance += credit_amount
        print("Credited Amount", (credit_amount), "Rupees", "\nNew Balance:", (self.balance), "Rupees")

    def print_balance(self):
        print("Your Remaining Balance is:", (self.balance), "Rupees")

a1 = Account(2000)
a1.debit(500)
a1.credit(1000)
a1.print_balance()




