import unittest
import fizz_app

class TestCase(unittest.TestCase):
    def test_add(self):
            self.assertEqual(fizz_app.fizz(1), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)