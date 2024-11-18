# Bannerizer
# Write a function that takes a short line of text and prints it within a box.
# Further Exploration
# Modify this function so that it truncates the message if 
# it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself).
# You may assume no maximum if the second argument is omitted.
# For a challenging but fun exercise, 
# try word wrapping messages that are too long to fit, 
# so that they appear on multiple lines but are still contained within the box. 
# This isn't an easy problem, but it's doable with basic Python.

def bannarizer(string):
    edge = '+' + ('-' + ('-' * len(string)) + '-') + '+'
    mid =  '|' + (' ' + (' ' * len(string)) + ' ') + '|'
    body = '|' + (' ' + (      string     ) + ' ') + '|'

    print(edge)
    print(mid)
    print(body)
    print(mid)
    print(edge)

# bannarizer('To boldly go where no one has gone before.')
# bannarizer('Welcome to Launch School')
# bannarizer('')

def bannarizer_updated(string, max_wdt = None):
    if max_wdt is None:
        max_wdt = len(string)

        edge = '+' + ('-' + ('-' * len(string)) + '-') + '+'
        mid =  '|' + (' ' + (' ' * len(string)) + ' ') + '|'
        body = '|' + (' ' + (      string     ) + ' ') + '|'
    else:
        edge = '+' + ('-' + ('-' * (max_wdt  - 4) ) + '-') + '+'
        mid =  '|' + (' ' + (' ' * (max_wdt  - 4) ) + ' ') + '|'
        body = '|' + (' ' + (string[:max_wdt - 4]) + ' ') + '|'

    print(edge)
    print(mid)
    print(body)
    print(mid)
    print(edge)

bannarizer_updated('To boldly go where no one has gone before.')
bannarizer_updated('To boldly go where no one has gone before.', 29)
bannarizer_updated('Welcome to Launch School')
bannarizer_updated('Welcome to Launch School', 11)
