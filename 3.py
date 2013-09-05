#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


class Node(object):
    def __init__(self, car=None, cdr=None):
        self.car = car
        if type(cdr) is Node or cdr is None:
            self.cdr = cdr
        else:
            raise(TypeError)

    def __str__(self):
        res = []
        i = self
        while(i.cdr):
            res.append(i.car)
            i = i.cdr
        res.append(i.car)
        res.append(i.cdr)
        return " -> ".join([str(x) for x in res])

    def __eq__(self, other):
        return self.car == other.car and self.cdr == other.cdr


class Stack(object):
    def __init__(self, node=Node()):
        if isinstance(node, Node):
            self.top = node
        else:
            raise TypeError

    def pop(self):
        if self.top:
            res = self.top.car
            self.top = self.top.cdr
            return res
        else:
            return None

    def push(self, d):
        nd = Node(d, self.top)
        self.top = nd

    def peek(self):
        return self.car


class SetOfStacks(object):
    _MAX_SIZE = 10

    def __init__(self, node=Node()):
        if isinstance(node, Node):
            self.top = node
        else:
            raise TypeError

    def pop(self):
        return None


class Queue(object):
    def __init__(self, head, tail):
        if isinstance(head, Node) and isinstance(tail, Node):
            self.head, self.tail = head, tail
        else:
            raise TypeError

    def enqueue(self, d):
        if self.head is None:
            self.last = Node(d, None)
            self.head = self.last
        else:
            self.tail.cdr = Node(d, None)
            self.tail = self.tail.cdr

    def dequeue(self):
        if self.head:
            res = self.head.car
            self.head = self.head.cdr
            return res
        else:
            return None

