import unittest
import palindrome

class TestChecker(unittest.TestCase):
   def test_is_pal(self):
       self.assertEqual(palindrome.check("кит на морі, романтик"), True)
   def test_not_pal(self):
       self.assertEqual(palindrome.check("кит на пляжі, романтик"), False)

if __name__ == "__main__":
    unittest.main()