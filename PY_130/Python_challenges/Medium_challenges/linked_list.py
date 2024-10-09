import unittest
'''
Simple Linked List
Write a simple linked list implementation.
The linked list is a fundamental data structure in computer science,
often used in the implementation of other data structures.

The simplest kind of linked list is a singly linked list.
Each element in the list contains data and a "next" field pointing to the next element in the list of elements.
This variant of linked lists is often used to represent sequences or push-down stacks (also called a LIFO stack; Last In, First Out).

Let's create a singly linked list whose elements may contain a range of data such as the numbers 1-10.
Provide methods to reverse the linked list and convert a linked list to and from a list.

'''

# Solution
'''
PEDAC
Problem:
    Input: Integers
    output: Integers

    Exp: Not much is gotten from the problem description but the test cases give you a good idea
    - A linked list where you can manipulate its elements using specific methods.
    - A variant of LIFO, last in, first out.
    - Elements can be a range of data, string, integers, etc,
    - Linked list can be reversed and convered from a link list to a list and vice versa.

    imp: From unnittest
    - Element class: Represents a single node in the linked list.
    - It holds a datum (data) and a reference to the next element (another node or None if it’s the last one).
    - There are properties and methods which do certain things:
    - datum: Get the data (datum) stored in the element.
    - next: Get the next element (next).
    - is_tail: Check if this element is the last one (is_tail).
        SimpleLinkedList class:
    - Represents the entire linked list, which is a collection of Element objects.
    - Attributes:
    - _head: The first node in the list.
    - _size: The number of elements in the list.
    - Methods:
    - push(datum): Adds a new element to the front of the list.
    - pop(): Removes and returns the first element from the list.
    - peek(): Looks at the first element’s data without removing it.
    - is_empty(): Checks if the list has no elements.
    - to_list(): Converts the linked list into a regular Python list.
    - from_list(input_list): Creates a linked list from a Python list.
    - reverse(): Returns a new linked list that’s the reverse of the current list.

Using unittest TestCase

Data Structure:
Class with class variables and methods.

Algorithm:
    - See the Implicit ideas
'''

class Element:
    def __init__(self, datum, next_element=None):
        self._datum = datum
        self._next = next_element

    @property
    def datum(self):
        return self._datum

    @property
    def next(self):
        return self._next

    def is_tail(self):
        return self.next is None

class SimpleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    @property
    def head(self):
        return self._head
    
    @property
    def size(self):
        return self._size

    def push(self, datum):
        self._head = Element(datum, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        datum = self._head.datum
        self._head = self._head.next
        self._size -= 1
        return datum

    def peek(self):
        return self._head.datum if self._head else None

    def is_empty(self):
        return self._size == 0

    def to_list(self):
        result = []
        current = self._head
        while current:
            result.append(current.datum)
            current = current.next
        return result
    
    @classmethod
    def from_list(cls, input_list):
        lst = cls()
        if input_list:
            for item in reversed(input_list):
                lst.push(item)
        return lst

    def reverse(self):
        reversed_list = SimpleLinkedList()
        current = self._head
        while current:
            reversed_list.push(current.datum)
            current = current.next
        return reversed_list

class LinkedListTest(unittest.TestCase):

    def test_element_datum(self):
        element = Element(1)
        self.assertEqual(1, element.datum)

    def test_element_tail(self):
        element = Element(1)
        self.assertTrue(element.is_tail())

    def test_element_next_default(self):
        element = Element(1)
        self.assertIsNone(element.next)

    def test_element_next_initialization(self):
        element1 = Element(1)
        element2 = Element(2, element1)
        self.assertEqual(element1, element2.next)

    def test_empty_list_size(self):
        lst = SimpleLinkedList()
        self.assertEqual(0, lst.size)

    def test_empty_list_empty(self):
        lst = SimpleLinkedList()
        self.assertTrue(lst.is_empty())

    def test_pushing_element_on_list(self):
        lst = SimpleLinkedList()
        lst.push(1)
        self.assertEqual(1, lst.size)

    def test_empty_list_1_element(self):
        lst = SimpleLinkedList()
        lst.push(1)
        self.assertFalse(lst.is_empty())

    def test_peeking_at_list(self):
        lst = SimpleLinkedList()
        lst.push(1)
        self.assertEqual(1, lst.size)
        self.assertEqual(1, lst.peek())

    def test_peeking_at_empty_list(self):
        lst = SimpleLinkedList()
        self.assertIsNone(lst.peek())

    def test_access_head_element(self):
        lst = SimpleLinkedList()
        lst.push(1)
        self.assertIsInstance(lst.head, Element)
        self.assertEqual(1, lst.head.datum)
        self.assertTrue(lst.head.is_tail())

    def test_items_are_stacked(self):
        lst = SimpleLinkedList()
        lst.push(1)
        lst.push(2)
        self.assertEqual(2, lst.size)
        self.assertEqual(2, lst.head.datum)
        self.assertEqual(1, lst.head.next.datum)

    def test_push_10_items(self):
        lst = SimpleLinkedList()
        for datum in range(1, 11):
            lst.push(datum)
        self.assertEqual(10, lst.size)
        self.assertEqual(10, lst.peek())

    def test_pop_1_item(self):
        lst = SimpleLinkedList()
        lst.push(1)
        self.assertEqual(1, lst.pop())
        self.assertEqual(0, lst.size)

    def test_popping_frenzy(self):
        lst = SimpleLinkedList()
        for datum in range(1, 11):
            lst.push(datum)
        for _ in range(6):
            lst.pop()
        self.assertEqual(4, lst.size)
        self.assertEqual(4, lst.peek())

    def test_from_a_empty_list(self):
        lst = SimpleLinkedList.from_list([])
        self.assertEqual(0, lst.size)
        self.assertIsNone(lst.peek())

    def test_from_a_nil(self):
        lst = SimpleLinkedList.from_list(None)
        self.assertEqual(0, lst.size)
        self.assertIsNone(lst.peek())

    def test_from_a_2_element_list(self):
        lst = SimpleLinkedList.from_list([1, 2])
        self.assertEqual(2, lst.size)
        self.assertEqual(1, lst.peek())
        self.assertEqual(2, lst.head.next.datum)

    def test_from_a_10_items(self):
        lst = SimpleLinkedList.from_list(list(range(1, 11)))
        self.assertEqual(10, lst.size)
        self.assertEqual(1, lst.peek())
        self.assertEqual(10, lst.head.next.next.next.next.next.next.next.next.next.datum)

    def test_to_a_empty_list(self):
        lst = SimpleLinkedList()
        self.assertEqual([], lst.to_list())

    def test_to_a_of_1_element_list(self):
        lst = SimpleLinkedList.from_list([1])
        self.assertEqual([1], lst.to_list())
        self.assertEqual(1, lst.size)
        self.assertEqual(1, lst.peek())

    def test_to_a_of_2_element_list(self):
        lst = SimpleLinkedList.from_list([1, 2])
        self.assertEqual([1, 2], lst.to_list())
        self.assertEqual(2, lst.size)
        self.assertEqual(1, lst.head.datum)
        self.assertEqual(2, lst.head.next.datum)

    def test_reverse_2_element_list(self):
        lst = SimpleLinkedList.from_list([1, 2])
        lst_r = lst.reverse()
        self.assertEqual(2, lst_r.peek())
        self.assertEqual(1, lst_r.head.next.datum)
        self.assertTrue(lst_r.head.next.is_tail())

    def test_reverse_10_element_list(self):
        data = list(range(1, 11))
        lst = SimpleLinkedList.from_list(data)
        self.assertEqual(data[::-1], lst.reverse().to_list())

    def test_roundtrip_10_element_list(self):
        data = list(range(1, 11))
        self.assertEqual(data, SimpleLinkedList.from_list(data).to_list())

if __name__ == '__main__':
    unittest.main() 

# # LS Solution ##
# class Element:
#     def __init__(self, datum, next_element=None):
#         self._datum = datum
#         self._next = next_element

#     @property
#     def datum(self):
#         return self._datum

#     @property
#     def next(self):
#         return self._next

#     def is_tail(self):
#         return self._next is None

# class SimpleLinkedList:
#     def __init__(self):
#         self._head = None

#     @property
#     def head(self):
#         return self._head

#     @property
#     def size(self):
#         size = 0
#         current_elem = self._head
#         while current_elem:
#             size += 1
#             current_elem = current_elem.next
#         return size

#     def is_empty(self):
#         return self._head is None

#     def push(self, datum):
#         element = Element(datum, self._head)
#         self._head = element

#     def peek(self):
#         return self._head.datum if self._head else None

#     def pop(self):
#         datum = self.peek()
#         if self._head:
#             self._head = self._head.next
#         return datum

#     @classmethod
#     def from_list(cls, lst=None):
#         if lst is None:
#             lst = []

#         linked_list = cls()
#         for datum in reversed(lst):
#             linked_list.push(datum)
#         return linked_list

#     def to_list(self):
#         lst = []
#         current_elem = self._head
#         while current_elem:
#             lst.append(current_elem.datum)
#             current_elem = current_elem.next
#         return lst

#     def reverse(self):
#         reversed_list = SimpleLinkedList()
#         current_elem = self._head
#         while current_elem:
#             reversed_list.push(current_elem.datum)
#             current_elem = current_elem.next
#         return reversed_list