import unittest
import num_check

class TestChecker(unittest.TestCase):
   def test_not_prime(self):
       self.assertEqual(num_check.check(4), True)
   def test_one(self):
       self.assertEqual(num_check.check(1), False)
   def test_prime(self):
       self.assertEqual(num_check.check(3), False)

if __name__ == "__main__":
    unittest.main()
