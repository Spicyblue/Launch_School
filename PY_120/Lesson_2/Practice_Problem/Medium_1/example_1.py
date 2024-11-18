'''
Example 1.

Alyssa asked Ben to code review the following code:

class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance

Ben glanced over the code quickly and said - "It looks fine, except that you're trying to
access self.balance instead of self._balance in the balance_is_positive method."

"Not so fast," Alyssa replied. "What I'm doing here is valid;
I can definitely use self.balance there!"

Who is correct, Ben or Alyssa? Why?

'''

# Solution


class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance

# Alyssa is right becuase the instance method `balance_is_positive` 
# calls the `balance` method which returns the self._balance value and 
# check if it is greater than zero and return the boolean result based on the operator evalutation

current_account = BankAccount(2000000)
print(current_account.balance_is_positive())

## LS Solution ##

# Alyssa is correct.
# By defining a property named balance that returns the value of self._balance,
# Alyssa can is write return self.balance > 0 with no trouble.
