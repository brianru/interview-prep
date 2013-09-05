import unittest
import copy
import pprint

def zero_row(mat, row):
    for x in xrange(0,len(mat[0])):
        mat[row][x] = 0
    return mat

def zero_col(mat, col):
    for x in xrange(0,len(mat)):
        mat[x][col] = 0
    return mat

def zero_out(mat):
    res = copy.deepcopy(mat) 
    for i in xrange(0,len(mat)):
        for j in xrange(0,len(mat[0])):
            if mat[i][j] == 0:
                res = zero_row(res, i)
                res = zero_col(res, j)
    return res

class ZeroOutTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(zero_out([[0, 1, 1]]),
                                  [[0, 0, 0]])
        self.assertEqual(zero_out([[0],
                                   [1],
                                   [1]]),
                                  [[0],
                                   [0],
                                   [0]])
        self.assertEqual(zero_out([[1,1,1],
                                   [0,1,1],
                                   [1,1,1]]),
                                  [[0,1,1],
                                   [0,0,0],
                                   [0,1,1]])
        self.assertEqual(zero_out([[1,1,1],
                                   [1,0,1],
                                   [0,1,1]]),
                                  [[0,0,1],
                                   [0,0,0],
                                   [0,0,0]])

if __name__ == "__main__":
    unittest.main()
