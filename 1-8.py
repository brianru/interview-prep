import unittest

def is_rotation(s1,s2):
    """Check if s2 is a rotation of s1, while only comparing the two strings a single time.
    s2 is a rotation of s1 if there is a point i, where:
    s2[i:] + s2[:i] == s1
       
    Or, just see if s2 is in s1s1...
    
    """
    return s2 in s1*2


class IsRotationTestCase(unittest.TestCase):
    def runTest(self):
        self.assertTrue(is_rotation("apple",
                                      "pleap"))
        self.assertTrue(is_rotation("brian","brian"))
        self.assertTrue(is_rotation("",""))
        self.assertTrue(is_rotation("hannah",
                                       "nahhan"))

if __name__ == "__main__":
    unittest.main()
