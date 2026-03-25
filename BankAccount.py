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


# Testing
acc = BankAccount("Sonit", 1000)
acc.deposit(500)
print(acc.get_balance())   # 1500

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
