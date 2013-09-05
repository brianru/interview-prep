#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


# You are given an array of integers (both positive and negative).
# Find the contiguous sequence with the largest sum. Return the sum.


def find_largest_seq(seq, res=0):
    """Dynamic programming!"""
    for i in xrange(len(seq)):
        res += max(find_largest_seq(seq[i:], res), res)
    return res

print find_largest_seq([2, 3, -8, -1, 2, 4, -2, 3])
