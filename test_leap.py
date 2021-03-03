import unittest
import leap_app

class TestCase(unittest.TestCase):
    def test_leap(self):
            self.assertEqual(leap_app.leap(2004), "Leap Year!")
            self.assertEqual(leap_app.leap(1900), "Not a leap year!")

if __name__ == '__main__':
    unittest.main(verbosity=2)