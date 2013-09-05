#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


def mastermind(guess, solution):
    if not isinstance(guess, str) and isinstance(solution, str):
        raise TypeError()
    if not len(guess) == len(solution):
        raise ValueError()
    hit, pseudo_hit = 0, 0
    for i in xrange(len(guess)-1):
        if guess[i] == solution[i]:
            hit += 1
            solution = solution[:i] + solution[i+1:]
    for i in xrange(len(guess)-1):
        if guess[i] in solution:
            pseudo_hit += 1
    return hit, pseudo_hit

# should return 1, 1
print mastermind("ggrr", "rgby")
