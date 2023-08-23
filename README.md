# Basic Unit Tests Template -- in this case using prime numbers (from CS50W)

Unit tests in Python are often written using Python's built-in unittest framework. This is an example that shows how you can create a suite of unit tests to test a function that checks if a given number is a prime number.

- prime.py: A function that checks for prime numbers
- test_prime.py: A file containing unit tests for the above function

In this example, the TestPrime class inherits from unittest.TestCase, which provides a framework for writing the tests. 

Each test is a method that begins with the word test. Inside each test method, you can use various assertion methods like assertTrue, assertFalse, assertEqual, etc., to check the behavior of your code.

- test_negative checks that negative numbers are not prime.
- test_zero_and_one checks that 0 and 1 are not prime.
- test_two checks that 2 is prime.
- test_other_primes checks that several other prime numbers are indeed prime.
- test_composites checks that composite numbers are not prime.

To run the tests, navigate to the folder containing both prime.py and test_prime.py in your terminal, and then run:

```bash
python -m unittest test_prime.py
```

This should execute all the test cases, and if your is_prime function is correct, all tests should pass.