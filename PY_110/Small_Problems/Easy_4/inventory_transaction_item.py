'''
Inventory Item Transactions.
Write a function that takes two arguments, an inventory item ID and a list of transactions,
and returns a list containing only the transactions for the specified inventory item.

# Problem
- Input: 
Integer and list of dictionary
- Output:
list of dictionary

- Rules
    Explicit:
    Function that takes two arguments, an inventory item ID and a list of transactions,.
    Returns a list containing only the transactions for the specified inventory item.
    Implicit:

# Examples

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

# Data structure
List and dictionary.

# Algorithm
    - High End:
        1. Get input.
        2. Create a list to hold result.
        3. Iterate through input list: (this returns the dictionaries in the list).
            - Create a dictionary values matches the item_id.
            - If yes, apppend the list element to the result.
        4.Return result.

# Code
'''

# Solution
def transactions_for(item_id, transaction_list):

    result = []

    for transactions in transaction_list:
        if transactions['id'] == item_id:
            result.append(transactions)

    return result

# # code check
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

# Note!
# Time take to write PEDAC and test/debug code is 18 mins, 10 seconds.

# Just needed to added a palindrome check to the original code.

## LS Answer ##
# def transactions_for(inventory_item, transactions):
#     return [transaction
#             for transaction in transactions
#             if transaction["id"] == inventory_item]
