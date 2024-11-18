'''
Wallet (Part 1).

Implement a Wallet class that represents a wallet with a certain amount of money.
You want to be able to combine (add) two wallets together
to get a new wallet with the combined total amount from both wallets.

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True

'''

# Solution

class Wallet:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented

        return Wallet(self.amount + other.amount)

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # Tru

## LS Solution ##

# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         if isinstance(other, Wallet):
#             return Wallet(self.amount + other.amount)

#         return NotImplemented

