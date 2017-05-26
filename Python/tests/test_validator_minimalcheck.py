import unittest
from tools import validator as v

class TestValidatorOfMinimalInt(unittest.TestCase):
    def test_correct_value(self):
        self.assertTrue(v.Validator.validateMinimalInt(3,20))

    def test_TypeError_when_no_value_is_input(self):
        with self.assertRaises(TypeError):
            v.Validator.validateMinimalInt()
            v.Validator.validateMinimalInt(2)

    def test_if_string(self):
        self.assertFalse(v.Validator.validateMinimalInt("ab", 2), 'This should return false due to: string in first argument.')
        self.assertFalse(v.Validator.validateMinimalInt(2, "ab"), 'This should return false due to: string in second argument.')

    def test_if_array_tuple_dict_first_arg(self):
        self.assertFalse(v.Validator.validateMinimalInt([1,2,3], 2), 'This should return false due to: array on first argument.')
        self.assertFalse(v.Validator.validateMinimalInt((1,2,3), 2), 'This should return false due to: tuple on first argument.')
        self.assertFalse(v.Validator.validateMinimalInt({1,2,3}, 2), 'This should return false due to: dictionary on first argument.')

    def test_if_array_tuple_dict_second_arg(self):
        self.assertFalse(v.Validator.validateMinimalInt(2, [1,2,3]), 'This should return false due to: array on second argument.')
        self.assertFalse(v.Validator.validateMinimalInt(2, (1,2,3)), 'This should return false due to: tuple on second argument.')
        self.assertFalse(v.Validator.validateMinimalInt(2, {1,2,3}), 'This should return false due to: dictionary on second argument.')

    def test_value_higher_minimal(self):
        self.assertFalse(v.Validator.validateMinimalInt(10, 5), 'This should return False.')

    def test_return_string_value_higher_minimal(self):
        v.Validator.validateMinimalInt(10, 5, warn = True)
        self.assertMultiLineEqual(v.warning, "Arguments must be below the limit. Put them below 5 or increase limit.")

    def test_value_equal_minimal(self):
        self.assertFalse(v.Validator.validateMinimalInt(10,10), 'This should return False.')

    def test_return_string_value_equal_minimal(self):
        v.Validator.validateMinimalInt(10, 10, warn = True)
        self.assertMultiLineEqual(v.warning, "The first value should not be equal to the minimal choosen.")



if __name__ == '__main__':
    unittest.main()
