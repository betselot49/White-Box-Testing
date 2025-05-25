import unittest
from count_letters import count_vowels_and_consonants

class TestCountVowelsAndConsonants(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_vowels_and_consonants(""), (0, 0))

    def test_only_vowels(self):
        self.assertEqual(count_vowels_and_consonants("aeiouAEIOU"), (10, 0))

    def test_only_consonants(self):
        self.assertEqual(count_vowels_and_consonants("bcdfgBCDFG"), (0, 10))

    def test_mixed_letters(self):
        self.assertEqual(count_vowels_and_consonants("Hello"), (2, 3))

    def test_mixed_with_non_alpha(self):
        self.assertEqual(count_vowels_and_consonants("He11o!"), (2, 2))  # '1' and '!' ignored





        
