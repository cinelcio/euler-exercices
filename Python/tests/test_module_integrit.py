import unittest
import validator as v

class TestValidatorWarning(unittest.TestCase):
    def test_warning_variable_empty(self):
        self.assertTrue(v.warning == "")


if __name__ == '__main__':
    unittest.main()
