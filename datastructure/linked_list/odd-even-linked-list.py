# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import InitList
from ListNode import ListNode


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy1, dummy2 = ListNode(0), ListNode(0)
        dummy1.next = head
        dummy2.next = head.next
        dummy3 = head.next
        count = 3
        while head and dummy3 and dummy3.next and head.next:
            if head.next.next and not dummy3.next.next:
                head.next = head.next.next
                head = head.next
                break
            elif not head.next.next and dummy3.next.next:
                dummy3.next = dummy3.next.next
                dummy3 = dummy3.next
                break
            if count%2:
                head.next = head.next.next
                head = head.next
            else:
                dummy3.next = dummy3.next.next
                dummy3 = dummy3.next
        head.next = dummy2.next
        if dummy3:
            dummy3.next = None
        return dummy1.next

if __name__=='__main__':
    l = [1,2,3,4,5,6,7,8]
    head = InitList.initlist(l)
    print Solution().oddEvenList(head)