class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Баланс пополнен на {amount}. Баланс: {self.balance}")
    def withdraw(self, amount):
        if not self.balance < amount:
            if amount <= 0:
                print("Ошибка. Вы ввели нулевую сумму, или отрицательную.")
            else:
                self.balance -= amount
                print(f"Вы вывели {amount}. Баланс: {self.balance}")
        else:
            print("Не хватает средств.")
    def show(self):
        print(f"Владелец: {self.owner}. Баланс: {self.balance}")
account = BankAccount("Аня")
account.deposit(500)
account.withdraw(300)
account.withdraw(3000)
account.show()