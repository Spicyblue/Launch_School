'''
Inventory Item Availability.
Building on the previous exercise, write a function that returns True or False
based on whether or not an inventory item (an ID number) is available.
As before, the function takes two arguments: an item ID and a list of transactions.
The function should return True only if the sum of the quantity values of the item's transactions is greater than zero.
Notice that there is a movement property in each transaction object.
A movement value of 'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.

# Problem
- Input: 
Integer and list of dictionary
- Output:
Bool

- Rules
    Explicit:
    Function should return True only if the sum of the quantity values of the item's transactions is greater than zero.
    A movement value of 'out' will decrease the item's quantity.
    A movement value of 'in' will increase the item's quantity.
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

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True

# Data structure
List and dictionary.

# Algorithm
    - High End:
        1. Get input.
        2. Create a counter for counting items going in and out.
        3. Iterate through input list: (this returns the dictionaries in the list).
            - Add quantity of items going in to counter for in.
            - Add quantity of items going out to counter for out. 
        4. Subtract quantity of items going in from out.
                - If the result is negative, return false.
                - if the result in positive, return True.

# Code
'''

# Solution
def transactions_for(item_id, transaction_list):

    result = []

    for transactions in transaction_list:
        if transactions['id'] == item_id:
            result.append(transactions)

    return result

def is_item_available(item_id, transaction_list):

    selected_transactions = transactions_for(item_id, transaction_list)

    all_in = 0
    all_out = 0

    for transactions in selected_transactions:
        if transactions["movement"] == 'in':
             all_in += transactions["quantity"]

        if transactions["movement"] == 'out':
            all_out += transactions["quantity"]

    total_left = all_in - all_out

    return total_left > 0

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

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True

# Note!
# Time take to write PEDAC and test/debug code is 10 mins, 10 seconds.

# Just needed to added a palindrome check to the original code.

## LS Answer ##
# def transactions_for(inventory_item, transactions):
#     return [transaction
#             for transaction in transactions
#             if transaction["id"] == inventory_item]

# def is_item_available(item, transactions):
#     relevant_transactions = transactions_for(item, transactions)
#     quantity = 0

#     for transaction in relevant_transactions:
#         if transaction["movement"] == 'in':
#             quantity += transaction["quantity"]
#         else:
#             quantity -= transaction["quantity"]

#     return quantity > 0