import unittest
from src.calculator import sum_numbers, subtract_numbers, multiply_numbers, divide_numbers

class TestAll(unittest.TestCase):
    def test_sum_numbers_positives(self):
        # Arrange
        num1 = num2 = 2
        expected_result = 4
        # Act
        result = sum_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_sum_numbers_negatives(self):
        # Arrange
        num1 = num2 = -2
        expected_result = -4
        # Act
        result = sum_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)


    def test_sum_numbers_floats(self):
        # Arrange
        num1 = 2.1
        num2 = 3.6
        expected_result = 5.7
        # Act
        result = sum_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_sum_numbers_integers_and_floats(self):
        # Arrange
        num1 = 2
        num2 = 3.6
        expected_result = 5.6
        # Act
        result = sum_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_sum_numbers_with_not_number_parameter(self):
        # Arrange
        num1 = 2
        num2 = "b"
        expected_result = TypeError
        # Act
        result = sum_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

  
    def test_subtract_numbers_positives(self):
        # Arrange
        num1 = num2 = 2
        expected_result = 0
        # Act
        result = subtract_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_subtract_numbers_negatives(self):
        # Arrange
        num1 = num2 = -2
        expected_result = 0
        # Act
        result = subtract_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_subtract_numbers_floats(self):
        # Arrange
        num1 = 3.6
        num2 = 2.1
        expected_result = 1.5
        # Act
        result = subtract_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_subtract_numbers_integers_and_floats(self):
        # Arrange
        num1 = 3.6
        num2 = 2
        expected_result = 1.6
        # Act
        result = subtract_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_subtract_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            subtract_numbers(1, "a")


    def test_multiply_numbers_positives(self):
        # Arrange
        num1 = 5
        num2 = 2
        expected_result = 10
        # Act
        result = multiply_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_multiply_numbers_negatives(self):
        # Arrange
        num1 = 5
        num2 = -2
        expected_result = -10
        # Act
        result = multiply_numbers(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)
        print(result)

    def test_multiply_numbers_floats(self):
        # Arrange
        num1 = 3.6
        num2 = 2.1
        expected_result = 7.56
        # Act
        result = multiply_numbers(num1, num2)
        # Assert
        self.assertAlmostEqual(result, expected_result)
        print(result)

    def test_multiply_numbers_integers_and_floats(self):
        # Arrange
        num1 = 3.6
        num2 = 2
        expected_result = 7.2
        # Act
        result = multiply_numbers(num1, num2)
        # Assert
        self.assertAlmostEqual(result, expected_result)
        print(result)

    def test_multiply_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(ValueError):
            multiply_numbers(1, "a")
            

    def test_divide_numbers_positives(self):
        # Arrange
        num1 = 5
        num2 = 2
        expected_result = 2.5
        # Act
        result = divide_numbers(num1, num2)
        # Assert
        self.assertAlmostEqual(result, expected_result)
        print(result)

    def test_divide_numbers_negatives(self):
        # Arrange
        num1 = 5
        num2 = -3
        expected_result = -1.6666666666666667
        # Act
        result = divide_numbers(num1, num2)
        # Assert
        self.assertAlmostEqual(result, expected_result)
        print(result)

    def test_divide_numbers_floats(self):
        # Arrange
        num1 = 3.6
        num2 = 2.1
        expected_result = 1.7142857142857142
        # Act
        result = divide_numbers(num1, num2)
        # Assert
        self.assertAlmostEqual(result, expected_result)
        print(result)

    def test_divide_numbers_integers_and_floats(self):
        # Arrange
        num1 = 3.6
        num2 = 2
        expected_result = 1.8
        # Act
        result = divide_numbers(num1, num2)
        # Assert
        self.assertAlmostEqual(result, expected_result)
        print(result)

    def test_divide_numbers_with_not_numbers(self):
        # Arrange
        num1 = "a"
        num2 = "b"
        expected_result = TypeError
        # Act
        result = divide_numbers(num1, num2)
        # Assert
        self.assertAlmostEqual(result, expected_result)
        print(result)

    # def test_divide_numbers_with_zero(self):
    #     # Arrange
    #     num1 = 3.6
    #     num2 = 0
    #     expected_result = "ZeroDivisionError"
    #     # Act
    #     result = divide_numbers(num1, num2)
    #     # Assert
    #     self.assertAlmostEqual(result, expected_result)
    #     print(result)        

if __name__ == '__main__':
    unittest.main()