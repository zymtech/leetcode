# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(8)
    #b = a
    print id(a),id(b)
