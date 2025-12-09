def calculate_least_squares():
    print("Linear regression coefficients calculation")
    print("=" * 40)

    try:
        n = int(input("Enter number of measurements: "))

        if n < 2:
            print("At least 2 measurements required!")
            return

        x_values=[]
        y_values=[]

        print("Enter measurements (x and y):")
        for i in range(n):
            x = float(input(f"x[{i + 1}] = "))
            y = float(input(f"y[{i + 1}] = "))
            x_values.append(x)
            y_values.append(y)

        sum_x = sum(x_values)
        sum_y = sum(y_values)
        sum_xy = sum(x*y for x, y in zip(x_values, y_values))
        sum_x2 = sum(x*x for x in x_values)

        denominator = n*sum_x2-sum_x*sum_x

        if abs(denominator)<1e-10:
            print("Error: all x values are the same, division by zero!")
            return

        a = (n*sum_xy-sum_x*sum_y)/denominator
        b = (sum_y-a*sum_x)/n

        print(f"\nResults:")
        print(f"Slope (a) = {a:.6f}")
        print(f"Intercept (b) = {b:.6f}")
        print(f"Regression equation: y = {a:.6f}x + {b:.6f}")

        return a, b

    except ValueError:
        print("Error: enter numbers")
        return None

def calculate_ls_coefficients(x_values, y_values):
    n = len(x_values)

    if n != len(y_values):
        raise ValueError("x and y must have same length")

    if n < 2:
        raise ValueError("At least 2 measurements required")

    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x*y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x*x for x in x_values)

    denominator = n*sum_x2-sum_x*sum_x

    if abs(denominator) < 1e-10:
        raise ZeroDivisionError("All x values are the same")

    a = (n*sum_xy-sum_x*sum_y)/denominator
    b = (sum_y-a*sum_x)/n

    return a, b

import unittest
from unittest.mock import patch
import io

class TestExercise6(unittest.TestCase):

    def test_perfect_line(self):
        x = [1, 2, 3, 4, 5]
        y = [5, 7, 9, 11, 13]
        a, b = calculate_ls_coefficients(x, y)
        self.assertAlmostEqual(a, 2.0, places=6)
        self.assertAlmostEqual(b, 3.0, places=6)

    def test_horizontal_line(self):
        x = [1, 2, 3, 4, 5]
        y = [4, 4, 4, 4, 4]
        a, b = calculate_ls_coefficients(x, y)
        self.assertAlmostEqual(a, 0.0, places=6)
        self.assertAlmostEqual(b, 4.0, places=6)

    def test_same_x_error(self):
        x = [2, 2, 2, 2, 2]
        y = [1, 2, 3, 4, 5]
        with self.assertRaises(ZeroDivisionError):
            calculate_ls_coefficients(x, y)

    def test_one_point_error(self):
        x = [1]
        y = [2]
        with self.assertRaises(ValueError):
            calculate_ls_coefficients(x, y)

    def test_different_lengths_error(self):
        x = [1, 2, 3]
        y = [1, 2]
        with self.assertRaises(ValueError):
            calculate_ls_coefficients(x, y)

    @patch('builtins.input', side_effect=['5', '1', '5', '2', '7', '3', '9', '4', '11', '5', '13'])
    def test_with_input(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = calculate_least_squares()

            output = mock_stdout.getvalue()
            self.assertIn("Linear regression coefficients calculation", output)
            self.assertIn("Enter number of measurements:", output)
            self.assertIn("Results:", output)
            self.assertIn("Slope (a)", output)
            self.assertIn("Intercept (b)", output)

            a, b = result
            self.assertAlmostEqual(a, 2.0, places=6)
            self.assertAlmostEqual(b, 3.0, places=6)

    @patch('builtins.input', side_effect=['1', '1', '2'])
    def test_one_point_input(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            calculate_least_squares()
            output = mock_stdout.getvalue()
            self.assertIn("At least 2 measurements required!", output)

    @patch('builtins.input', side_effect=['3', '2', '1', '2', '2', '2', '3'])
    def test_same_x_input(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            calculate_least_squares()
            output = mock_stdout.getvalue()
            self.assertIn("all x values are the same", output)

    @patch('builtins.input', side_effect=['abc'])
    def test_invalid_input(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            calculate_least_squares()
            output = mock_stdout.getvalue()
            self.assertIn("Error: enter numbers!", output)

if __name__=='__main__':
    unittest.main()