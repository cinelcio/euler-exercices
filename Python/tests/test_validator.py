import unittest
from tools import validator as v


class TestValidatorOfPositiveInt(unittest.TestCase):
    def test_validation_of_None(self):
        self.assertEqual(v.Validator.validatePositiveInt(None), None)

    def test_if_all_arguments_are_not_int(self):
        self.assertFalse(v.Validator.validatePositiveInt("ab"), 'This parameter should return False')
        self.assertFalse(v.Validator.validatePositiveInt([1,2,3]), 'This parameter should return False')
        self.assertFalse(v.Validator.validatePositiveInt((1,2,3)), 'This parameter should return False')
        self.assertFalse(v.Validator.validatePositiveInt({1,2,3}), 'This parameter should return False')

    def test_return_string_not_int(self):
        v.Validator.validatePositiveInt("ab",True)
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: ab.")
        v.Validator.validatePositiveInt([1,2,3],True)
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: [1, 2, 3].")
        v.Validator.validatePositiveInt((1,2,3),True)
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: (1, 2, 3).")
        v.Validator.validatePositiveInt({1,2,3},True)
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: {1, 2, 3}.")

    def test_not_negative_numbers(self):
        self.assertFalse(v.Validator.validatePositiveInt(-1))
        self.assertFalse(v.Validator.validatePositiveInt(-1,7))

    def test_return_string_negative_numbers(self):
        v.Validator.validatePositiveInt(-1)
        self.assertMultiLineEqual(v.warning, "Only positive integers are allowed. -1 is negative.")
        v.Validator.validatePositiveInt(-1,2)
        self.assertMultiLineEqual(v.warning, "Only positive integers are allowed. -1 is negative.")

    def test_zero(self):
        self.assertEqual(0, v.Validator.validatePositiveInt(0), 'This should return False due to value zero')

    def test_return_string_zero(self):
        v.Validator.validatePositiveInt(0,True)
        self.assertMultiLineEqual(v.warning, "The argument value is 0 (zero).")

    def test_correct_input(self):
        self.assertTrue(v.Validator.validatePositiveInt(3), 'This should return True.')

    def test_return_string_correct_input(self):
        v.Validator.validatePositiveInt(3)
        self.assertMultiLineEqual(v.warning, "The data is a positive integer higher than 0 (zero).")

    # def test_warn_argument(self):
    #     self.assertMultiLineEqual(print(v.Validator.validatePositiveInt(3, warn = True)), "True\nThe data is a positive integer higher than 0 (zero).")
    #     self.self.assertFalse(v.Validator.validatePositiveInt(), 'message')

    def test_TypeError_when_no_value_is_input(self):
        with self.assertRaises(TypeError):
            v.Validator.validatePositiveInt()
        # self.self.assertEqual(expected, actual, 'message')

# class TestValidatorOfMinimalInt(object):
    # def test_validateMinimalInt(self):
    #     self.assertFalse(v.Validator.validatePositiveInt(1,2,-20))

if __name__ == '__main__':
    unittest.main()
