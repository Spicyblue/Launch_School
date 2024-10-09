import unittest
'''
Create a custom set type.

Sometimes it is necessary to define a custom data structure of some type.
In some languages, including Python, there is a built-in Set type.
For this problem, you're expected to implement your own custom set type.
How it works internally doesn't matter, as long as it behaves like a set of unique elements that can be manipulated in several well defined ways.
Once you've reached a solution, feel free to play around with using the built-in implementation of Set.
For simplicity, you may assume that all elements of a set must be numbers.

'''

# Solution
'''
PEDAC
Problem:
    Input: integers
    output:  set

    Exp: Not much is gotten from the problem description but the test cases give you a good idea.
    - Create a custome set class.
'''

class CustomSet:
    def __init__(self, elements=None):
        self.elements = []
        if elements:
            for element in elements:
                self.add(element)

    def is_empty(self):
        return len(self.elements) == 0

    def contains(self, element):
        return element in self.elements

    def is_subset(self, other):
        return all(other.contains(element) for element in self.elements)

    def is_disjoint(self, other):
        return all(not other.contains(element) for element in self.elements)

    def is_same(self, other):
        return self.is_subset(other) and other.is_subset(self)

    def add(self, element):
        if not self.contains(element):
            self.elements.append(element)

    def intersection(self, other):
        return CustomSet([element for element in self.elements if other.contains(element)])

    def difference(self, other):
        return CustomSet([element for element in self.elements if not other.contains(element)])

    def union(self, other):
        new_set = CustomSet(self.elements)
        for element in other.elements:
            new_set.add(element)
        return new_set

    def __eq__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        return self.is_same(other)

class CustomSetTest(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(CustomSet().is_empty())

    def test_not_empty(self):
        set = CustomSet([1])
        self.assertFalse(set.is_empty())

    def test_empty_does_not_contain(self):
        set = CustomSet()
        self.assertFalse(set.contains(1))

    def test_does_contain(self):
        set = CustomSet([1, 2, 3])
        self.assertTrue(set.contains(1))

    def test_set_does_not_contain(self):
        set = CustomSet([1, 2, 3])
        self.assertFalse(set.contains(4))

    def test_subset_empty(self):
        empty_set = CustomSet()
        self.assertTrue(empty_set.is_subset(CustomSet()))

    def test_empty_is_subset_of_non_empty(self):
        empty_set = CustomSet()
        self.assertTrue(empty_set.is_subset(CustomSet([1])))

    def test_non_empty_not_subset_of_empty(self):
        set = CustomSet([1])
        self.assertFalse(set.is_subset(CustomSet()))

    def test_set_is_subset_of_same_set_of_elements(self):
        set = CustomSet([1, 2, 3])
        self.assertTrue(set.is_subset(CustomSet([1, 2, 3])))

    def test_set_is_subset_of_larger_set(self):
        set = CustomSet([1, 2, 3])
        self.assertTrue(set.is_subset(CustomSet([4, 1, 2, 3])))

    def test_not_subset_when_different_elements(self):
        set = CustomSet([1, 2, 3])
        self.assertFalse(set.is_subset(CustomSet([4, 1, 3])))

    def test_disjoint_empty_set(self):
        empty_set = CustomSet()
        self.assertTrue(empty_set.is_disjoint(CustomSet()))

    def test_disjoint_empty_and_non_empty(self):
        empty_set = CustomSet()
        self.assertTrue(empty_set.is_disjoint(CustomSet([1])))

    def test_disjoint_non_empty_and_empty(self):
        set = CustomSet([1])
        self.assertTrue(set.is_disjoint(CustomSet()))

    def test_disjoint_shared_element(self):
        set = CustomSet([1, 2])
        self.assertFalse(set.is_disjoint(CustomSet([2, 3])))

    def test_disjoint_no_shared_elements(self):
        set = CustomSet([1, 2])
        self.assertTrue(set.is_disjoint(CustomSet([3, 4])))

    def test_equal_empty(self):
        empty_set = CustomSet()
        self.assertTrue(empty_set.is_same(CustomSet()))

    def test_equal_empty_and_non_empty(self):
        empty_set = CustomSet()
        self.assertFalse(empty_set.is_same(CustomSet([1, 2, 3])))

    def test_equal_non_empty_and_empty(self):
        set = CustomSet([1, 2, 3])
        self.assertFalse(set.is_same(CustomSet()))

    def test_equal_same_elements(self):
        set = CustomSet([1, 2])
        self.assertTrue(set.is_same(CustomSet([2, 1])))

    def test_equal_different_elements(self):
        set = CustomSet([1, 2, 3])
        self.assertFalse(set.is_same(CustomSet([1, 2, 4])))

    def test_equal_duplicate_elements_do_not_matter(self):
        set = CustomSet([1, 2, 2, 1])
        self.assertTrue(set.is_same(CustomSet([2, 1])))

    def test_add_to_empty(self):
        set = CustomSet()
        set.add(3)
        self.assertEqual(set, CustomSet([3]))

    def test_add_to_non_empty(self):
        set = CustomSet([1, 2, 4])
        set.add(3)
        self.assertEqual(set, CustomSet([1, 2, 4, 3]))

    def test_add_existing_element(self):
        set = CustomSet([1, 2, 3])
        set.add(3)
        self.assertEqual(set, CustomSet([1, 2, 3]))

    def test_intersection_empty(self):
        set = CustomSet().intersection(CustomSet())
        self.assertEqual(set, CustomSet())

    def test_intersection_empty_and_non_empty(self):
        set = CustomSet().intersection(CustomSet([3, 2, 5]))
        self.assertEqual(set, CustomSet())

    def test_intersection_non_empty_and_empty(self):
        set = CustomSet([3, 2, 5]).intersection(CustomSet())
        self.assertEqual(set, CustomSet())

    def test_intersection_no_shared_elements(self):
        first_set = CustomSet([1, 2, 3])
        second_set = CustomSet([4, 5, 6])
        actual = first_set.intersection(second_set)
        self.assertEqual(actual, CustomSet())

    def test_intersection_shared_elements(self):
        first_set = CustomSet([1, 2, 3, 4])
        second_set = CustomSet([3, 2, 5])
        actual = first_set.intersection(second_set)
        self.assertEqual(actual, CustomSet([2, 3]))

    def test_difference_empty(self):
        actual = CustomSet().difference(CustomSet())
        self.assertEqual(actual, CustomSet())

    def test_difference_empty_and_non_empty(self):
        actual = CustomSet().difference(CustomSet([3, 2, 5]))
        self.assertEqual(actual, CustomSet())

    def test_difference_non_empty_and_empty(self):
        actual = CustomSet([1, 2, 3, 4]).difference(CustomSet())
        self.assertEqual(actual, CustomSet([1, 2, 3, 4]))

    def test_difference_non_empty_sets(self):
        actual = CustomSet([3, 2, 1]).difference(CustomSet([2, 4]))
        self.assertEqual(actual, CustomSet([3, 1]))

    def test_union_empty(self):
        actual = CustomSet().union(CustomSet())
        self.assertEqual(actual, CustomSet())

    def test_union_empty_and_non_empty(self):
        actual = CustomSet().union(CustomSet([2]))
        self.assertEqual(actual, CustomSet([2]))

    def test_union_non_empty_and_empty(self):
        actual = CustomSet([1, 3]).union(CustomSet())
        self.assertEqual(actual, CustomSet([1, 3]))

    def test_union_non_empty_sets(self):
        actual = CustomSet([1, 3]).union(CustomSet([2, 3]))
        self.assertEqual(actual, CustomSet([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()

# # LS Solution ##
# class CustomSet:
#     def __init__(self, elements=None):
#         if elements is None:
#             elements = []
#         self._elements = []
#         for el in elements:
#             if el not in self._elements:
#                 self._elements.append(el)

#     def is_empty(self):
#         return len(self._elements) == 0

#     def intersection(self, other_set):
#         same_elements = [el for el in self._elements if other_set.contains(el)]
#         return CustomSet(same_elements)

#     def union(self, other_set):
#         union_set = CustomSet(self._elements)
#         for el in other_set._elements:
#             union_set.add(el)
#         return union_set

#     def difference(self, other_set):
#         different_elements = [el for el in self._elements if not other_set.contains(el)]
#         return CustomSet(different_elements)

#     def is_disjoint(self, other_set):
#         return all(not other_set.contains(el) for el in self._elements)

#     def is_same(self, other_set):
#         if len(self._elements) != len(other_set._elements):
#             return False
#         return all(other_set.contains(el) for el in self._elements)

#     def is_subset(self, other_set):
#         return all(other_set.contains(el) for el in self._elements)

#     def add(self, element):
#         if element not in self._elements:
#             self._elements.append(element)
#         return self

#     def contains(self, element):
#         return element in self._elements

#     def __eq__(self, other_set):
#         return self.is_same(other_set)