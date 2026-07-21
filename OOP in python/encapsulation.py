class Bank:
    def __init__(self):
        self.balance=1000

    def deposit(self,amount):
        self.balance+=amount

    def show(self):
        print("Balance:",self.balance)

b=Bank()
b.deposit(500)
b.show()
