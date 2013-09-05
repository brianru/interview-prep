import copy


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


def cons(v, n):
    return Node(v, n)


def linked_list(it):
    tail = Node(it[-1], None)
    for x in xrange(2, len(it)+1):
        head = Node(it[-x], tail)
        tail = head
    return head


def dedupe(linked_list):
    """Exercises 2-1"""
    items = [linked_list.car]
    last, cur = linked_list, linked_list.cdr
    while(cur):
        if cur.car in items:
            last.cdr = cur.cdr  # skip cur in the list
            cur = cur.cdr
        else:
            items.append(cur.car)
            last, cur = cur, cur.cdr
    return linked_list


def find_kth_to_last(head, k):
    """Exercise 2-2"""
    res, runner = head, head
    for i in xrange(1, k+1):
        runner = runner.cdr
    while(runner.cdr is not None):
        res = res.cdr
        runner = runner.cdr
    return res

def remove_node(nd):
    """Exercise 2-3"""
    next_node = nd.cdr
    nd.car, nd.cdr = next_node.car, next_node.cdr


def insert_after(head, val):
    if head is None:
        return Node(val, head)
    else:
        temp = Node(val, head.cdr)
        head.cdr = temp
        return head


def insert_before(head, val):
    if head is None:
        return Node(val, head)
    else:
        temp = copy.deepcopy(head)
        head.car = val
        head.cdr = temp
        return head


def partition_list(head, val):
    """Exercise 2-4"""
    before, after = None, None
    while(head):
        next = head.cdr
        if head.car < val:  # insert head to start of before list
            head.cdr = before
            before = head
        else:  # insert head into start of after list
            head.cdr = after
            after = head
        head = next
    if before is None:
        return after
    head = before
    while(before.cdr):
        before = before.cdr
    before.cdr = after
    return head


def add_lists(x, y):
    """Exercise 2-5"""
    res = None
    rem = 0
    while x and y:
        s = x.car + y.car
        a, rem = s % 10, s / 10
        if rem is not 0:
            if res:
                res.car += rem
            else:
                res = insert_before(res, rem)
        res = insert_before(res, a)
        x, y = x.cdr, y.cdr
    return res


def reverse(linked_list):
    res = None
    while linked_list:
        res = insert_before(res, linked_list.car)
        linked_list = linked_list.cdr
    return res


def add_lists2(x, y):
    """Exercise 2-5 follow-up

    """
    return reverse(add_lists(reverse(x), reverse(y)))


def add_to_end(head, node):
    nd = head
    while nd.cdr:
        nd = nd.cdr
    nd.cdr = node


def find_cycle(ls):
    """Exercise 2-6"""
    seen = [(ls.car, ls.cdr.car)]
    while ls.cdr:
        nxt = ls.cdr
        if (nxt.car, nxt.cdr.car) in seen:
            return (nxt.car, nxt.cdr.car)
        else:
            seen.append((nxt.car, nxt.cdr.car))
            ls = nxt
    return False


def is_palindrome(ls):
    """Exercise 2-7"""
    return ls == reverse(ls)


