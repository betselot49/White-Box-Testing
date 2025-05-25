import unittest
from prime_utils import is_prime

class TestIsPrime(unittest.TestCase):
    def test_negative(self):
        self.assertFalse(is_prime(-5))

    def test_zero_and_one(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))

    def test_small_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))

    def test_large_prime(self):
        self.assertTrue(is_prime(29))

    def test_large_non_prime(self):
        self.assertFalse(is_prime(100))





