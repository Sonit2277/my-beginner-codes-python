import json
#exceptions
class InsufficientFundsError(Exception):
    pass
class InvalidAmountError(Exception):
    pass
class NegativeBalanceError(Exception):
    pass
class TransactionLimitExceededError(Exception):
    pass
#base class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    def get_owner(self):
        return self.owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

    def loan(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Loan amount must be positive.")

    def repay_loan(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Repayment amount exceeds current balance.")
        else:
            print("Repayment amount must be positive.")

    def transfer(self, amount, target_account):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                target_account.deposit(amount)
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")

    def save_account(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount to save must be positive.")

    def withdraw_savings(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient savings for withdrawal.")
        else:
            print("Amount to withdraw must be positive.")

    def account_number(self):
        return f"{self.owner[:3].upper()}-{id(self) % 10000:04d}"

    def transaction_history(self):
        # Placeholder for transaction history implementation
        return "Transaction history is not implemented yet."

    def checking_account(self):
        return f"Checking account for {self.owner}"    

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.owner == other.owner and self.__balance == other.__balance
        return False

    def __hash__(self):
        return hash((self.owner, self.__balance))

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"
    
    def statement(self):
        print(f"Account: {self.account_number} | Owner: {self.owner}")
        # Note: __transactions is not defined in this class
        # This method needs a transaction history implementation
#Subclasses    
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"SavingsAccount(owner={self.owner}, balance={self.balance}, interest_rate={self.interest_rate})"
    
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance + self.overdraft_limit:
            print("Insufficient funds including overdraft limit.")
        else:
            self.balance -= amount

    def transfer(self, amount, target_account):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                target_account.deposit(amount)
            else:
                print("Insufficient funds for transfer including overdraft limit.")
        else:
            print("Transfer amount must be positive.")

    def repay_loan(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
            else:
                print("Repayment amount exceeds current balance including overdraft limit.")
        else:
            print("Repayment amount must be positive.")

    def __str__(self):
        return f"CheckingAccount(owner={self.owner}, balance={self.balance}, overdraft_limit={self.overdraft_limit})"
    

    
def main():
    acc = BankAccount("Sonit", 1000)
    acc.deposit(500)
    print(acc.get_balance())   # 1500

    acc.withdraw(200)
    print(acc.get_balance())   # 1300

    acc.set_balance(2000)
    print(acc.get_balance())   # 2000

    acc.loan(500)
    print(acc.get_balance())   # 2500

    acc.repay_loan(300)
    print(acc.get_balance())   # 2200

    acc.transfer(200, BankAccount("Alice", 500))
    print(acc.get_balance())   # 2000

    acc.save_account(300)
    print(acc.get_balance())   # 2300

    acc.withdraw_savings(100)
    print(acc.get_balance())   # 2200

#persistence
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
    if data["type"] == "SavingsAccount":
        return SavingsAccount(data["owner"], data["account_number"], data["balance"])
    elif data["type"] == "CheckingAccount":
        return CheckingAccount(data["owner"], data["account_number"], data["balance"])
    return BankAccount(data["owner"], data["account_number"], data["balance"])

def test_persistence():
    acc = SavingsAccount("Sonit", 1500, 0.02)
    save_account(acc, "account.json")
    loaded_acc = load_account("account.json")
    print(loaded_acc)  # Should show the same account details as acc

# Run tests
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


# Testing
acc = BankAccount("Sonit", 1000)
acc.deposit(500)
print(acc.get_balance())   # 1500

CheckingAccount=CheckingAccount("Sonit", 1000, 500)
CheckingAccount.withdraw(1200)  # Should allow due to overdraft
print(CheckingAccount.get_balance())  # -200

SavingsAccount=SavingsAccount("Sonit", 1500, 0.02)
SavingsAccount.apply_interest()

acc.withdraw(200)
print(acc.get_balance())   # 1300

acc.set_balance(2000)
print(acc.get_balance())   # 2000

acc.loan(500)
print(acc.get_balance())   # 2500

acc.repay_loan(300)
print(acc.get_balance())   # 2200

acc.transfer(200, BankAccount("Alice", 500))
print(acc.get_balance())   # 2000

acc.save_account(300)
print(acc.get_balance())   # 2300

acc.withdraw_savings(100)
print(acc.get_balance())   # 2200

acc.statement()  # Account statement for Sonit
print(acc.statement())    # Account: SON-1234 | Owner: Sonit
acc.account_number()  # e.g., SON-1234
print (acc.account_number())  # e.g., SON-1234
print(acc.transaction_history())  # Transaction history is not implemented yet.
print(acc.checking_account())  # Checking account for Sonit

acc.save_account(500)
print(acc.get_balance())   # 2700
acc2 = BankAccount("Alice", 500)
acc.transfer(200, acc2)
print(acc.get_balance())   # 1800
print(acc2.get_balance())  # 700

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass



try:
    acc.balance = -500  # ValueError
except ValueError as e:
    print("Error:", e)

try:
    acc.set_balance(-100)  # Balance cannot be negative.
except ValueError as e:
    print("Error:", e)




try:
    print(acc.__balance)   # AttributeError
except AttributeError as e:
    print("Error:", e)

print(acc._BankAccount__balance)  # works because of name mangling

acc.withdraw(200)
print(acc.get_balance())   # 1300


acc2 = BankAccount("S", 1300)
acc3 = BankAccount("o", 1300)

print(acc == acc2)  # False
print(acc == acc3)  # False
print(acc == acc)   # True
print(acc2 == acc2) # True
print(acc3 == acc3) # True

print(acc)          # BankAccount(owner=Sonit, balance=1300)
print(repr(acc))    # BankAccount(owner=Sonit, balance=1300)

print(hash(acc))    
print(hash(acc2))   
print(hash(acc3))   

print(hash(acc) == hash(acc2))   # usually False
print(hash(acc) == hash(acc3))   # usually False
print(hash(acc2) == hash(acc3))  # usually False
print(hash(acc) == hash(acc))    # True
print(hash(acc2) == hash(acc2))  # True

accounts_set = {acc, acc2, acc3}
print(accounts_set)

print(acc in accounts_set)  
print(acc2 in accounts_set)  
print(acc3 in accounts_set)  

print(BankAccount("Sonit", 1300) in accounts_set)  # True
print(BankAccount("Sonit", 1500) in accounts_set)  # False
print(BankAccount("Alice", 1300) in accounts_set)  # False
