#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


class Node(object):
    def __init__(self, data=None, neighbors=[]):
        self.data, self.neighbors = data, neighbors
        self.visited = False

    def visit(self):
        self.visited = True

    def route_to(self, target):
        if self is target:
            return True
        for nd in [i for i in self.neighbors if not i.visited]:
            nd.visit()
            if nd.route_to(target):
                return True
        return False

