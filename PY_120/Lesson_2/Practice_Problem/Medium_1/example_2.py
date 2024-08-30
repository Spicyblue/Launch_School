'''
Example 2.

Alan created the following code to keep track of items for a shopping cart application he's writing:

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10_000

Without changing any of the above lines of code,
update the InvoiceEntry class so it functions as shown.
'''

# Solution

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self._quantity = other

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10_000

## LS Solution ##

# To make this program work as shown, 
# we need to add a getter and setter property to the InvoiceEntry class.
# The getter is needed to ensure that the two print function invocations produce output,
# while the setter is needed to ensure that entry.quantity = 10_000 works.

# class InvoiceEntry:
#     def __init__(self, product_name, number_purchased):
#         self._product_name = product_name
#         self._quantity = number_purchased

#     @property
#     def quantity(self):
#         return self._quantity

#     @quantity.setter
#     def quantity(self, quantity):
#         self._quantity = quantity

# entry = InvoiceEntry('Marbles', 5000)
# print(entry.quantity)         # 5000

# entry.quantity = 10_000
# print(entry.quantity)         # 10_000