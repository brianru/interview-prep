import unittest
from pprint import pprint


def rotate_90 (mat):
    """http://questiontrack.com/how-does-this-code-snippet-rotating-a-matrix-work-1051237.html"""
    return [list(a) for a in zip(*mat[::-1])]

class Rotate90TestCase(unittest.TestCase):
    def runTest(self):
        pprint(rotate_90([[1,2],[3,4]]))
        self.assertEqual(rotate_90([[1, 2], [3, 4]]), [[3, 1], [4, 2]])

if __name__ == "__main__":
    unittest.main()
