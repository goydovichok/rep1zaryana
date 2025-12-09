def factorize_number():
    try:
        n = int(input("Enter a natural number greater than 1:"))

        if n <= 1:
            print("Number must be greater than 1")
            return

        print(f"Prime factors of {n}:")

        factors=[]
        original_n=n
        divisor=2

        while n>1:
            while n%divisor==0:
                factors.append(divisor)
                n//=divisor
            divisor+=1 if divisor==2 else 2

        if len(factors)==1:
            print(f"{original_n} = {factors[0]} (prime number)")
        else:
            result = " × ".join(map(str, factors))
            print(f"{original_n} = {result}")

        return factors

    except ValueError:
        print("Error: enter an integer!")
        return None

def factorize_number_function(n):
    if n<=1:
        raise ValueError("Number must be greater than 1")

    factors=[]
    divisor=2

    while n>1:
        while n%divisor==0:
            factors.append(divisor)
            n//=divisor
        divisor+=1 if divisor==2 else 2

    return factors

import unittest
from unittest.mock import patch
import io

class TestExercise2(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertEqual(factorize_number_function(2), [2])
        self.assertEqual(factorize_number_function(13), [13])
        self.assertEqual(factorize_number_function(17), [17])

    def test_composite_numbers(self):
        self.assertEqual(factorize_number_function(4), [2, 2])
        self.assertEqual(factorize_number_function(6), [2, 3])
        self.assertEqual(factorize_number_function(12), [2, 2, 3])
        self.assertEqual(factorize_number_function(100), [2, 2, 5, 5])

    def test_large_number(self):
        result = factorize_number_function(360)
        self.assertEqual(result, [2, 2, 2, 3, 3, 5])

    def test_errors(self):
        with self.assertRaises(ValueError):
            factorize_number_function(1)
        with self.assertRaises(ValueError):
            factorize_number_function(0)
        with self.assertRaises(ValueError):
            factorize_number_function(-5)

    @patch('builtins.input', return_value='12')
    def test_with_input(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            factors = factorize_number()

            output = mock_stdout.getvalue()
            self.assertIn("Enter a natural number greater than 1:", output)
            self.assertIn("Prime factors of 12:", output)
            self.assertIn("12 = 2 × 2 × 3", output)
            self.assertEqual(factors, [2, 2, 3])

    @patch('builtins.input', return_value='1')
    def test_input_one(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            factorize_number()
            output = mock_stdout.getvalue()
            self.assertIn("Number must be greater than 1!", output)

    @patch('builtins.input', return_value='abc')
    def test_invalid_input(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            factorize_number()
            output = mock_stdout.getvalue()
            self.assertIn("Error: enter an integer!", output)

if __name__=='__main__':
    unittest.main()