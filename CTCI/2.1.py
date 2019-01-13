# Q) 2.1: Write code to remove duplicates from an unsorted linked list.
#code
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            
            a = ListNode(0)
            a.next = head
            b = a
            l = []
            while b.next != None:
                b = b.next
                l.append(b.val)
            
            l = sorted(list(set(l)))
            c = ListNode(0)
            d = c
            for itm in l:
                c.next = ListNode(itm)
                c= c.next

            return d.next