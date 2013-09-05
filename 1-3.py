import unittest

def permutation (s1, s2):
    return sorted(s1) == sorted(s2)

class PermutationTestCase(unittest.TestCase):
    def runTest(self):
        self.assertTrue(permutation("brian", "ianrb"))
        self.assertFalse(permutation("brian", "hannah"))
        self.assertTrue(permutation("",""))

if __name__ == "__main__":
    unittest.main()        
