#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


class TreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class ListNode(object):
    def __init__(self, car=None, cdr=None):
        self.car, self.cdr = car, cdr


def cons(n, l):
    return ListNode(n, l)


def to_linked_lists(root, depth=1, res=None):
    if res is None:
        res = []
    while len(res) < depth:
        res.append(ListNode())
    res[depth] = cons(root, res[depth])
    if root.left:
        to_linked_lists(root.left, depth+1, res)
    if root.right:
        to_linked_lists(root.right, depth+1, res)
    return res


