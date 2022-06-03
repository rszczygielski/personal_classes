import unittest
from unittest import TestCase

class ExampleTest(TestCase):
    def testTest(self):
        a = 1
        b = 3
        self.assertEqual(a+b, 4)


if __name__ == "__main__":
    unittest.main()