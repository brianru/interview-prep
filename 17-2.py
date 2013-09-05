#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Design an algorithm to figure out if someone has won a game of tic-tac-toe.


def has_won(board):
    """ input: board is an NxN array containing
               0s for empty spaces,
               1s for player 1's moves,
               2s for player 2's moves

    """
    # check diagonals
    # top left to bottom right board[i][i]
    cand = board[0][0]
    n = set([board[i][i] for i in xrange(len(board))])
    if len(n) == 1 and 0 not in n:
        return cand

    # top right to bottom left board[-i][i]
    cand = board[0][-1]
    n = set([board[i][-(i+1)] for i in xrange(len(board))])
    if len(n) == 1 and 0 not in n:
        return cand

    # check rows
    for i in xrange(len(board)):
        n = set(board[i])
        if len(n) == 1 and 0 not in n:
            return board[i][0]

    # check columns
    for i in xrange(len(board)):
        n = set([board[j][i] for j in xrange(len(board))])
        if len(n) == 1 and 0 not in n:
            return board[0][i]

a = [[0 for row in xrange(10)] for col in xrange(10)]
for i in xrange(10):
    a[i][-(i+1)] = 1
print(has_won(a))

