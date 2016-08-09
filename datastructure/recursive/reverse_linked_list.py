# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    """recursive solution"""
    def reverseList(self, head):
        if not head or not head.next:
            return head
        dummy = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return dummy


class Solution2(object):
    """iterative solution"""
   # @param {ListNode} head
   # @return {ListNode}
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next


if __name__=='__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print head
    print Solution2().reverseList(head)
    print Solution().reverseList(head)
