# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p, q = head, 0
        
        while l1 or l2:
            r = q
            if l1:
                r += l1.val
                l1 = l1.next
            if l2:
                r += l2.val
                l2 = l2.next
            q, r = divmod(r, 10)
            p.next = ListNode(r)
            p = p.next
        
        if q == 1:
            p.next = ListNode(1)
            
        return head.next