# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class InitList(object):
    @classmethod
    def initlist(self, l):
        if not l:
            return None
        dummy = ListNode(0)
        head = ListNode(l[0])
        dummy.next = head
        count = 1
        while count <len(l):
            head.next = ListNode(l[count])
            count += 1
            head = head.next
        return dummy.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(8)
    #b = a
    #print id(a),id(b)
    print InitList.initlist([1,2,3])
