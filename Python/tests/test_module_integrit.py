import unittest
from tools import validator

class TestValidatorWarning(unittest.TestCase):
    def test_warning_variable_empty(self):
        v = validator.Validator()
        self.assertTrue(v.warning == "")


if __name__ == '__main__':
    unittest.main()
