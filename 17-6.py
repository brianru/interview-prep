#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


# Given an array of integers, write a method to find indices m and n
# such that if you sorted elements m through n,
# the entire array would be sorted.
# Minimize n - m (that is, find the smallest such sequence).


def find_unsorted_sequence(seq):
    m, n = 0, len(seq) - 1  # index of last element in seq
    while seq[m] <= seq[m+1]:
        m += 1
    while seq[n] >= seq[n-1]:
        n -= 1
    seq_min, seq_max = min(seq[m:n]), max(seq[m:n])
    while seq[m] >= seq_min:
        m -= 1
    while seq[n] <= seq_max:
        n += 1
    return m, n


seq = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
m, n = find_unsorted_sequence(seq)
print "left: %s" % seq[:m]
print "middle: %s" % seq[m:n]
print "right: %s" % seq[n:]
print "sorted: %s" % (seq[:m] + sorted(seq[m:n]) + seq[n:])

