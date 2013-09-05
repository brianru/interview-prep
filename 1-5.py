import unittest

def compress_str(s):
    res = ''
    last = s[0]
    count = 0
    for i in s:
        if last == i:
            count += 1
        else:
            res += last + str(count)
            last, count = i, 1
    res += last + str(count)
    if len(res) < len(s):
        return res
    else:
        return s

class CompressStrTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(compress_str("aaaabaaaa"), "a4b1a4")
        self.assertEqual(compress_str("aa"),"aa")

if __name__ == "__main__":
    unittest.main()
        
    
