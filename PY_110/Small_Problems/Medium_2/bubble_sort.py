'''
Bubble Sort
Bubble Sort is one of the simplest sorting algorithms available.
It is not an efficient algorithm, so developers rarely use it in real code.
However, it is an excellent exercise for student developers.
In this exercise, you will write a function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list.
On each pass, the two values of each pair of consecutive elements are compared.
If the first value is greater than the second, the two elements are swapped.
This process is repeated until a complete pass is made without performing any swaps.
At that point, the list is completely sorted.

We can stop iterating the first time we make a pass through the list without
making any swaps since that means the entire list is sorted.

For further information -- including pseudo-code that demonstrates the algorithm,
as well as a minor optimization technique -- see the Bubble Sort Wikipedia page.

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above.
The sorting should be done "in-place" -- that is, the function should mutate the list.
You may assume that the list contains at least two elements.

# Problem
- Input: 
list
- Output:
list

- Rules
    Explicit:
    - Mutates the list passed as an argument.
    - List contains at least two elements.

    Implicit:

# Examples
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

# Data structure
List

# Algorithm
   Pseudocode from wikipedia available at https://en.wikipedia.org/wiki/Bubble_sort
   
   procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped := false
        for i := 1 to n-1 inclusive do
            { if this pair is out of order }
            if A[i-1] > A[i] then
                { swap them and remember something changed }
                swap(A[i-1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure
# Code
'''

# Solution
def swap(lst, idx):
    first = lst[idx]
    second = lst[idx + 1]

    lst[idx] = second
    lst[idx + 1] = first

def bubble_sort(lst):
    lst_len = len(lst)
    sorting =  True

    while sorting:
        swapped = False

        for idx in range(lst_len - 1):
            if lst[idx] > lst[idx + 1]:
                swap(lst, idx)
                print(lst)  # Just to see the changes being made.
                swapped = True

        if not swapped: # This is important because it checks if  `swapped` is falsy, and it would only be falsy when all the items in the list can't be swapped(are ordered).
            sorting = False

    return lst

# code check
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

# Note!

# Note!
# Time take to write PEDAC and test/debug code is isnt available since i got the pseudocode from Wikipedia.
# However, it is was easy to covert to code and the logic was more cool.


## LS Answer ##
# def bubble_sort(lst):
#     while True:
#         swapped = False
#         for idx in range(1, len(lst)):
#             if lst[idx - 1] <= lst[idx]:
#                 continue

#             lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
#             swapped = True

#         if not swapped:
#             break