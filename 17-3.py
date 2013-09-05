#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


def count_fives(n):
    fives = 0
    while(n % 5 == 0):
        fives += 1
        n /= 5
    return fives


def num_zeros(n):
    """Find the number of trailing zeros in n!

    Find the number of pairs of 5 and an even number.
    If a number is a multiple of 5, count the number of factors of 5.

    """
    num_evens, num_fives = 0, 0
    for i in xrange(1, n + 1):
        if i % 5 == 0:
            num_fives += count_fives(i)
        if i % 2 == 0:
            num_evens += 1
    return min(num_evens, num_fives)


