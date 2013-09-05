#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def isbalanced(self):
        """Exercise 4-1"""
        return abs(self.left.height() - self.right.height()) <= 1

    def height(self, cur=1):
        """Traverse down the tree incrementing a height variable."""
        if self.left is None and self.right is None:
            return cur
        elif self.left is None:
            return self.right.height(cur+1)
        elif self.right is None:
            return self.left.height(cur+1)
        else:
            return max(self.left.height(cur+1),
                       self.right.height(cur+1))



