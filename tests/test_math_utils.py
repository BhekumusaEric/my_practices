"""
Test cases for math_utils.py
These tests will help you understand exactly what your functions should do.
"""

import unittest
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math_utils import fibonacci_sequence, is_prime, prime_factors, gcd, lcm


class TestMathUtils(unittest.TestCase):
    
    def test_fibonacci_sequence_basic(self):
        """Test basic Fibonacci sequence generation"""
        result = fibonacci_sequence(8)
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        self.assertEqual(result, expected)
    
    def test_fibonacci_sequence_small_values(self):
        """Test Fibonacci with small values"""
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(3), [0, 1, 1])
    
    def test_fibonacci_sequence_negative(self):
        """Test Fibonacci with negative input"""
        result = fibonacci_sequence(-5)
        self.assertEqual(result, [])
    
    def test_fibonacci_sequence_large(self):
        """Test Fibonacci with larger sequence"""
        result = fibonacci_sequence(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)
    
    def test_is_prime_basic_primes(self):
        """Test is_prime with known prime numbers"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            self.assertTrue(is_prime(prime), f"{prime} should be prime")
    
    def test_is_prime_basic_non_primes(self):
        """Test is_prime with known non-prime numbers"""
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]
        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime), f"{non_prime} should not be prime")
    
    def test_is_prime_edge_cases(self):
        """Test is_prime with edge cases"""
        self.assertFalse(is_prime(1))   # 1 is not prime
        self.assertFalse(is_prime(0))   # 0 is not prime
        self.assertFalse(is_prime(-5))  # Negative numbers are not prime
        self.assertFalse(is_prime(-2))  # Even negative numbers are not prime
    
    def test_is_prime_large_numbers(self):
        """Test is_prime with larger numbers"""
        self.assertTrue(is_prime(97))   # Large prime
        self.assertTrue(is_prime(101))  # Large prime
        self.assertFalse(is_prime(100)) # Large composite
        self.assertFalse(is_prime(99))  # Large composite (3 * 33)
    
    def test_prime_factors_basic(self):
        """Test basic prime factorization"""
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(15), [3, 5])
        self.assertEqual(prime_factors(17), [17])  # Prime number
        self.assertEqual(prime_factors(1), [])
    
    def test_prime_factors_powers_of_primes(self):
        """Test prime factorization of powers of primes"""
        self.assertEqual(prime_factors(8), [2, 2, 2])    # 2^3
        self.assertEqual(prime_factors(9), [3, 3])       # 3^2
        self.assertEqual(prime_factors(25), [5, 5])      # 5^2
        self.assertEqual(prime_factors(16), [2, 2, 2, 2]) # 2^4
    
    def test_prime_factors_larger_numbers(self):
        """Test prime factorization of larger numbers"""
        self.assertEqual(prime_factors(30), [2, 3, 5])
        self.assertEqual(prime_factors(60), [2, 2, 3, 5])
        self.assertEqual(prime_factors(100), [2, 2, 5, 5])
    
    def test_prime_factors_edge_cases(self):
        """Test prime factorization edge cases"""
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(3), [3])
        self.assertEqual(prime_factors(4), [2, 2])
    
    def test_gcd_basic(self):
        """Test basic GCD calculations"""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 13), 1)  # Coprime numbers
        self.assertEqual(gcd(100, 25), 25)
        self.assertEqual(gcd(12, 8), 4)
    
    def test_gcd_edge_cases(self):
        """Test GCD edge cases"""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(7, 7), 7)  # Same numbers
    
    def test_gcd_order_independence(self):
        """Test that GCD is order-independent"""
        self.assertEqual(gcd(48, 18), gcd(18, 48))
        self.assertEqual(gcd(100, 25), gcd(25, 100))
    
    def test_gcd_negative_numbers(self):
        """Test GCD with negative numbers"""
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)
    
    def test_lcm_basic(self):
        """Test basic LCM calculations"""
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(17, 13), 221)  # Coprime numbers: 17 * 13
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(5, 7), 35)
    
    def test_lcm_edge_cases(self):
        """Test LCM edge cases"""
        self.assertEqual(lcm(1, 5), 5)
        self.assertEqual(lcm(5, 1), 5)
        self.assertEqual(lcm(7, 7), 7)  # Same numbers
    
    def test_lcm_with_zero(self):
        """Test LCM with zero"""
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 0), 0)
    
    def test_lcm_order_independence(self):
        """Test that LCM is order-independent"""
        self.assertEqual(lcm(12, 18), lcm(18, 12))
        self.assertEqual(lcm(4, 6), lcm(6, 4))
    
    def test_gcd_lcm_relationship(self):
        """Test the relationship between GCD and LCM"""
        # For any two numbers a and b: GCD(a,b) * LCM(a,b) = |a * b|
        test_pairs = [(12, 18), (17, 13), (4, 6), (100, 25)]
        
        for a, b in test_pairs:
            gcd_val = gcd(a, b)
            lcm_val = lcm(a, b)
            self.assertEqual(gcd_val * lcm_val, abs(a * b),
                           f"GCD({a},{b}) * LCM({a},{b}) should equal |{a} * {b}|")
    
    def test_mathematical_properties(self):
        """Test various mathematical properties"""
        # Test that prime factorization works correctly
        for n in [12, 15, 30, 60]:
            factors = prime_factors(n)
            product = 1
            for factor in factors:
                product *= factor
                self.assertTrue(is_prime(factor), f"{factor} should be prime")
            self.assertEqual(product, n, f"Product of prime factors should equal {n}")


if __name__ == '__main__':
    unittest.main()
