import unittest

def reverse (s):
    """Reverse a string"""
    res = ""
    for x in s:
        res = x + res
    return res

class ReverseTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("12345"), "54321")

if __name__ == "__main__":
    unittest.main()
