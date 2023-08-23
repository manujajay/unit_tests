import unittest
from prime import is_prime  # Make sure that 'prime.py' is in the same directory

class TestPrime(unittest.TestCase):

    def test_negative(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-10))
        self.assertFalse(is_prime(-999))

    def test_zero_and_one(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_other_primes(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))

if __name__ == "__main__":
    unittest.main()
