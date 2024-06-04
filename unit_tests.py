import unittest
import sys

def can_drive(age):
   driving_age = 16
   return age >= driving_age

class TestCanDrive(unittest.TestCase):

    # basic functionality
    def test_age_at_driving_age(self):
        self.assertTrue(can_drive(16))

    def test_age_below_driving_age(self):
        self.assertFalse(can_drive(15))

    def test_age_above_driving_age(self):
        self.assertTrue(can_drive(17))

    # boundary values
    def test_just_below_driving_age(self):
        self.assertFalse(can_drive(15.9))
        
    def test_just_above_driving_age(self):
        self.assertTrue(can_drive(16.1))

    # extreme values
    def test_min_value(self):
        self.assertFalse(can_drive(-sys.maxsize - 1))

    def test_min_value_plus_one(self):
        self.assertFalse(can_drive(-sys.maxsize))

    def test_max_value(self):
        self.assertTrue(can_drive(sys.maxsize))

    def test_max_value_minus_one(self):
        self.assertTrue(can_drive(sys.maxsize - 1))
        
    # other tests
    def test_negative_age(self):
        self.assertFalse(can_drive(-1))
        
    def test_zero_age(self):
        self.assertFalse(can_drive(0))

    def test_non_integer_string_input(self):
        with self.assertRaises(TypeError):
            can_drive("sixteen")

if __name__ == '__main__':
   unittest.main()