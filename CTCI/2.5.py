# Q) 2.5: Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
#DEFINITION
#Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list.
#EXAMPLE
#input: A -> B -> C -> D -> E -> C [the same C as earlier]
#output: C
#code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            slowPtr = head
            slowPtr=slowPtr.next
            fastPtr = head
            if slowPtr:
                fastPtr = slowPtr.next
            else:
                return None
            while slowPtr != None:
                
                if slowPtr is fastPtr:
                    break
                    
                elif fastPtr!=None:
                    if fastPtr.next != None:
                        fastPtr = fastPtr.next.next
                    else:
                        return None
                else:
                    return None
                slowPtr=slowPtr.next
            
            pt1 = head
            pt2 = slowPtr
            while pt1!= pt2:
                pt1 =pt1.next
                pt2 =pt2.next
            return pt1
                
            
        else:
            return None