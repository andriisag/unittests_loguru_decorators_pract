import unittest
import str_to_list

class TestChecker(unittest.TestCase):
   def test(self):
       self.assertEqual(str_to_list.check("hello, biden"), ["hello", "biden"])

if __name__ == "__main__":
    unittest.main()