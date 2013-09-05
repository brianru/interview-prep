import unittest

def unique_chars (s):
    """Determine if a string has all unique characters."""
    for i in xrange(0,len(s)):
        if s[i] in s[:i]:
            return False
    return True

class Exer_1_1_TestCase(unittest.TestCase):
    def runTest(self):
        self.assertTrue(unique_chars("brian"))
        self.assertTrue(unique_chars(""))
        self.assertFalse(unique_chars("apple"))

if __name__ == "__main__":
    unittest.main()
