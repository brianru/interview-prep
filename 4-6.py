#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


class TreeNode(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def next(node):
    """Find the next node in a binary search tree.

    Cases:
        - right child
        ---> traverse up until you're not the right child
        ---> return that node

        - left child
        ---> return parent

        - no parent or right child
        ---> return None

    """
    if is_right_child(node):


def is_right_child(node):
    return node.parent.right is node


def is_left_child(node):
    return node.parent.left is left

