import unittest
from unittest import TestCase
from unittest.mock import patch

from utils import factorial, super_factorial


class FactorialTestCase(TestCase):
    def test_factorial_5(self):
        n = 5
        result = factorial(n)
        expected_result = 120
        self.assertEqual(result, expected_result)

    def test_factorial_10(self):
        n = 10
        result = factorial(n)
        expected_result = 3628800
        self.assertEqual(result, expected_result)


class SuperFactorial(TestCase):
    def setUp(self) -> None:
        self.number = 5
        self.float = 5.1
        self.string = '5'
        self.less_zero_number = -5

    # интеграционный тест
    def test_integer_number(self):
        result = super_factorial(self.number)
        expected_result = 120
        self.assertEqual(result, expected_result)

    # юниттест =)
    @patch('utils.factorial')
    def test_integer_number_factorial_mock(self, mock_factorial):
        mock_factorial.return_value = 120
        result = super_factorial(self.number)
        expected_result = 120
        self.assertEqual(result, expected_result)

    def test_float_number(self):
        with self.assertRaises(Exception) as e:
            super_factorial(self.float)
        self.assertEqual('this must be an integer number', e.exception.args[0])

    def test_string_number(self,):
        with self.assertRaises(Exception) as e:
            super_factorial(self.string)
        self.assertEqual('this must be an integer number', e.exception.args[0])

    def test_less_zero_number(self):
        with self.assertRaises(Exception) as e:
            super_factorial(self.less_zero_number)
        self.assertEqual('the number must be more than 0', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
