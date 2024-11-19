import unittest
'''
Point Mutations.
Write a program that can calculate the Hamming distance
between two DNA strands.

A mutation is simply a mistake that occurs during the creation
or copying of a nucleic acid, in particular DNA.
Because nucleic acids are vital to cellular functions,
mutations tend to cause a ripple effect throughout the cell.
Although mutations are technically mistakes,
a very rare mutation may equip the cell with a beneficial attribute.
In fact, the macro effects of evolution are attributable to the accumulated result
of beneficial microscopic mutations over many generations.

The simplest and most common type of nucleic acid mutation is a point mutation,
which replaces one base with another at a single nucleotide.

By counting the number of differences between two homologous DNA strands
taken from different genomes with a common ancestor,
we get a measure of the minimum number of point mutations
that could have occurred on the evolutionary path between the two strands.

This is called the Hamming distance.

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
The Hamming distance between these two DNA strands is 7.

The Hamming distance is only defined for sequences of equal length.
If you have two sequences of unequal length,
you should compute the Hamming distance over the shorter length.

'''

# Solution
'''
PEDAC
Problem:
    Input: String
    output: integers

    Exp: 
    - Hamming distance is the difference between base pairs of two sequences.
    - Sequences must be of equall length.
    - if sequence have different lenght, compute the distance over the shorter lenght


    imp:
    - unittest test cases show that our we need a DNA class which accepts strings passed to the constructor.
    - The triangle class should have a method hamming_distance which accpets one argument (also a string).
    - The hamming_distance is the difference between the DNA instance variable and the method instance variable.

Examples:
Using unittest TestCase


Data Structure:
Class with instance variables and methods

Algorithm:
    Highend
    - Get the first sequence and the second sequence
    - Get the hamming distance between the both sequence.
    - Return the hamming distance.


    Lowend:
        - Define a class DNA which has accepts one argument using the DNA constructor. 
        - Set this to an instance variable _first_sequence.
        - Define an instance method hamming_distance which accepts one argument.
        - Set this to an instance variable _second_sequqence.
        - Initialize a counter to 0.
        - Set a len_of_shortest_seq variable and assign it the lenght of the shorted sequence.
            - Iterate through _first_sequence and _second_sequqence simultaneously, 
               ending at the shortest sequence,
                - Check if the currnet element in _first_sequence is difference from the current element of _second_sequqence.
                    - If yes , increase counter by 1.

            Return the value of counter. 
'''

class DNA:

    def __init__(self, first_seq):
        self._first_sequence = first_seq

    def hamming_distance(self, second_seq):
        self._second_sequqence = second_seq

        len_of_shortest_seq = len(min(self._first_sequence,
                                      self._second_sequqence,
                                      key = len))

        count = 0
        for idx in range(0, len_of_shortest_seq):
            if self._first_sequence[idx] != self._second_sequqence[idx]:
                count += 1

        return count

class TestDNAMutations(unittest.TestCase):
    def test_no_difference_between_empty_strands(self):
        self.assertEqual(0, DNA("").hamming_distance(""))

    def test_no_difference_between_identical_strands(self):
        self.assertEqual(0, DNA("GGACTGA").hamming_distance("GGACTGA"))

    def test_complete_hamming_distance_in_small_strand(self):
        self.assertEqual(3, DNA("ACT").hamming_distance("GGA"))

    def test_hamming_distance_in_off_by_one_strand(self):
        strand = "GGACGGATTCTGACCTGGACTAATTTTGGGG"
        distance = "AGGACGGATTCTGACCTGGACTAATTTTGGGG"
        self.assertEqual(19, DNA(strand).hamming_distance(distance))

    def test_small_hamming_distance_in_middle_somewhere(self):
        self.assertEqual(1, DNA("GGACG").hamming_distance("GGTCG"))

    def test_larger_distance(self):
        self.assertEqual(2, DNA("ACCAGGG").hamming_distance("ACTATGG"))

    def test_ignores_extra_length_on_other_strand_when_longer(self):
        self.assertEqual(3, DNA("AAACTAGGGG").hamming_distance("AGGCTAGCGGTAGGAC"))

    def test_ignores_extra_length_on_original_strand_when_longer(self):
        strand = "GACTACGGACAGGGTAGGGAAT"
        distance = "GACATCGCACACC"
        self.assertEqual(5, DNA(strand).hamming_distance(distance))

    def test_does_not_actually_shorten_original_strand(self):
        dna = DNA("AGACAACAGCCAGCCGCCGGATT")
        self.assertEqual(1, dna.hamming_distance("AGGCAA"))
        self.assertEqual(4, dna.hamming_distance("AGACATCTTTCAGCCGCCGGATTAGGCAA"))
        self.assertEqual(1, dna.hamming_distance("AGG"))

if __name__ == "__main__":
    unittest.main()

## LS Solution ##

# class DNA:
#     def __init__(self, strand):
#         self.strand = strand

#     def hamming_distance(self, comparison):
#         differences = 0

#         for char1, char2 in zip(self.strand, comparison):
#             if char1 != char2:
#                 differences += 1

#         return differences
