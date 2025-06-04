"""
Problem 6: Mathematical Operations
Recursive/iterative algorithms and mathematical problem-solving
"""

def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Returns:
        list: List containing the first n Fibonacci numbers
        
    Note:
        - Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
        - F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1
        - For n <= 0, return empty list
        
    Example:
        fibonacci_sequence(8) -> [0, 1, 1, 2, 3, 5, 8, 13]
        fibonacci_sequence(0) -> []
        fibonacci_sequence(1) -> [0]
        fibonacci_sequence(2) -> [0, 1]
    """
    # TODO: Implement this function (iterative approach recommended)
    pass


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is prime, False otherwise
        
    Note:
        - Prime numbers are greater than 1 and only divisible by 1 and themselves
        - 1 is not considered prime
        - Negative numbers are not prime
        
    Example:
        is_prime(17) -> True
        is_prime(4) -> False
        is_prime(1) -> False
        is_prime(-5) -> False
    """
    # TODO: Implement this function
    pass


def prime_factors(n):
    """
    Find all prime factors of a number.
    
    Args:
        n (int): Positive integer to factorize
        
    Returns:
        list: List of prime factors in ascending order (with repetition)
        
    Example:
        prime_factors(12) -> [2, 2, 3]
        prime_factors(17) -> [17]
        prime_factors(1) -> []
    """
    # TODO: Implement this function
    pass


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of two numbers using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest Common Divisor of a and b
        
    Example:
        gcd(48, 18) -> 6
        gcd(17, 13) -> 1
        gcd(0, 5) -> 5
    """
    # TODO: Implement this function using Euclidean algorithm
    pass


def lcm(a, b):
    """
    Calculate the Least Common Multiple of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Least Common Multiple of a and b
        
    Note: LCM(a,b) = |a*b| / GCD(a,b)
        
    Example:
        lcm(12, 18) -> 36
        lcm(17, 13) -> 221
    """
    # TODO: Implement this function (use your gcd function)
    pass
