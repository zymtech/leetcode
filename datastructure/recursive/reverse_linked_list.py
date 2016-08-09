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
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        while dummy.next:
            dummy = dummy.next
        if not head:
            return None
        while head.next:
            self.redirect(head, head.next)
        return dummy

    def redirect(self, left, right):
        if right.next is None:
            right.next = left
            return left
        else:
            self.redirect(left.next, right.next)

class Solution2(object):
    """non-recursive, iterative solution"""
   # @param {ListNode} head
   # @return {ListNode}
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            print dummy.next
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next


if __name__=='__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    #print head
    #print Solution().reverseList(head)
    print Solution2().reverseList(head)