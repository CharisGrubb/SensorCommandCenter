
from SensorCommandCenter.Database.IOValidation import InputOutputValidation as IOV
import unittest 


class Authorization_Tests(unittest.TestCase):

    def test_valid_username(self):
        
        self.assertEqual('admin', IOV.validate_user_name('admin'))
        
    def test_invalid_username(self):
        # from SensorCommandCenter.Database.IOValidation import InputOutputValidation
        self.assertRaises(Exception, IOV.validate_user_name, "' OR 1=1--")

class db_tests(unittest.TestCase):

    def test_input_injection(self):
        pass


if __name__ == '__main__':
    unittest.main()