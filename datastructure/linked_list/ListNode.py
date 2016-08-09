# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

if __name__ == '__main__':
    b = ListNode(0)
    a = ListNode(1)
    b.next = a
    a.val = 2
    print b,a
    print a.val, b.val