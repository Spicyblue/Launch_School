'''
Calendar Event Checker.
We have a list of events and want to check whether a specific date is available 
(i.e., no events planned for that date).
However, the function always returns the wrong value.
'''

# # Current code
# events = {
#     "2023-08-13": ["Python debugging exercises"],
#     "2023-08-14": ["Read 'Automate the Boring Stuff'"],
#     "2023-08-15": ["Webinar: Python for Data Science"],
# }

# def is_date_available(date):
#     if date in events:
#         return True

#     return False

# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True

'''
Issue with the current code:
The current code checks if the `date` argument being pass is a key in events,
and return `True` if is a value (an event) instead of `False`.
It also return False for an invalid key (`date`).

To solve this, we need to check if the `key` argument is not in the dictionary,
and return `True` and if is, return `False`.
However this does not update the dictionary with the new key.
'''

# fixed code 
events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date not in events:
        return True

    return False
print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

# Note!
# Time take to debug code is 1 mins, 12 seconds.
# Took more time to write the reason for the error but didnt include it.

## LS Answer ##
# def is_date_available(date):
#     if date not in events:
#         return True

#     return False

