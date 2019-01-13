# Q) 2.2: Implement an algorithm to find the nth to last element of a singly linked list.
#code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head:
            fastPtr = head
            slowPtr = head
            while n > 0:
                fastPtr = fastPtr.next
                n -=1
            if fastPtr:
                
                while fastPtr.next != None:
                    prev = slowPtr
                    slowPtr = slowPtr.next
                    fastPtr = fastPtr.next

                slowPtr.next = slowPtr.next.next
                return head
            else:
                head = slowPtr.next
                return head	