import json

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        if balance < 0:
            raise InvalidAmountError("Balance cannot be negative")
        self.__balance = balance
        self.__transactions = []

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise InvalidAmountError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit must be positive.")
        self.__balance += amount
        self.__transactions.append(f"Deposited {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.__balance -= amount
        self.__transactions.append(f"Withdrew {amount:.2f}")

    def transfer(self, amount, target):
        if amount <= 0:
            raise InvalidAmountError("Transfer must be positive.")
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.__balance -= amount
        target.deposit(amount)
        self.__transactions.append(f"Transferred {amount:.2f} to {target.owner}")

    def statement(self):
        print(f"-- {self.account_number} | {self.owner} --")
        for t in self.__transactions[-5:]:
            print(f"  {t}")
        print(f"  Balance: {self.__balance:.2f}")

    def __str__(self):
        return f"BankAccount({self.owner}, {self.__balance:.2f})"

    def __repr__(self):
        return f"BankAccount({self.owner!r}, {self.account_number!r}, {self.__balance!r})"


class SavingsAccount(BankAccount):
    def __init__(self, owner, account_number, balance=0, interest_rate=0.04):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.balance * self.interest_rate)

    def __str__(self):
        return f"SavingsAccount({self.owner}, {self.balance:.2f}, rate={self.interest_rate})"


class CheckingAccount(BankAccount):
    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise InsufficientFundsError("Exceeds overdraft limit.")
        self.balance -= amount

    def __str__(self):
        return f"CheckingAccount({self.owner}, {self.balance:.2f}, overdraft={self.overdraft_limit})"


def save_account(account, filename):
    data = {
        "type": type(account).__name__,
        "owner": account.owner,
        "account_number": account.account_number,
        "balance": account.balance
    }
    with open(filename, "w") as f:
        json.dump(data, f)

def load_account(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    t = data["type"]
    if t == "SavingsAccount":
        return SavingsAccount(data["owner"], data["account_number"], data["balance"])
    elif t == "CheckingAccount":
        return CheckingAccount(data["owner"], data["account_number"], data["balance"])
    return BankAccount(data["owner"], data["account_number"], data["balance"])


if __name__ == "__main__":
    s = SavingsAccount("Sonit", "SAV001", 10000)
    c = CheckingAccount("Rahul", "CHK001", 500, overdraft_limit=1000)

    s.apply_interest()
    s.transfer(2000, c)
    c.withdraw(1400)

    try:
        c.withdraw(500)
    except InsufficientFundsError as e:
        print("Caught:", e)

    s.statement()
    c.statement()

    save_account(s, "sonit_savings.json")
    s2 = load_account("sonit_savings.json")
    print(s2)