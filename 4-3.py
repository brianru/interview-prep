#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bst(data):
    """Find the median, set as root, set left and right children to
    recursive calls to bst on the left and right halves of input array.

    """
    l = len(data)
    if l is 0:
        return None
    elif l is 1:
        return Node(data[l])
    else:
        return Node(value=data[l/2],
                    left=bst(data[:l/2]),
                    right=bst(data[l/2+1:]))

