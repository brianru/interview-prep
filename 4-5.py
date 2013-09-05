#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


class TreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(root):
    if root is None:  # if leaf, OK
        return True
    elif root.left and not root.left.value <= root.value:
        # verify left <= root
        return False
    elif root.right and not root.right.value > root.value:
        # verify right > root
        return False
    else:
        # verify children are also bst's
        return is_bst(root.left) and is_bst(root.right)

