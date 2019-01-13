# Q) 2.4: You have two numbers represented by a linked list, where each node contains a single digit. 
# 	The digits are stored in reverse order, such that the 1’s digit is at the head of the list. 
# 	Write a function that adds the two numbers and returns the sum as a linked list.
#	EXAMPLE:
#		Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
#		Output: 8 -> 0 -> 8
#code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        sum_list = ListNode(0)
        a = sum_list
        carry = 0
        while c1 != None or c2 != None:
            
            if c1 and c2:
                if c1.val + c2.val >= 10:
                    
                    
                    sum_list.next = ListNode((c1.val + c2.val) - 10 + carry)
                    carry = 1
                else:
                    if carry + c1.val+c2.val >= 10:
                        carry = 1
                        sum_list.next = ListNode((c1.val + c2.val) - 10 + carry)
                    else:
                        
                        sum_list.next = ListNode(carry + c1.val+c2.val)
                        carry = 0
                sum_list = sum_list.next
                c1 = c1.next
                c2 = c2.next
            if c1 and not c2:
                if carry + c1.val >= 10:
                    carry = 1
                    sum_list.next = sum_list.next = ListNode((0+ c1.val) - 10 + carry)
                else:
                    
                    sum_list.next = ListNode(carry + 0+c1.val)
                    carry = 0
                sum_list = sum_list.next
                c1 = c1.next
            if c2 and not c1:
                if carry + c2.val >= 10:
                    carry = 1
                    sum_list.next = sum_list.next = ListNode((0+ c2.val) - 10 + carry)
                else:
                    
                    sum_list.next = ListNode(carry + 0+c2.val)
                    carry = 0
                sum_list = sum_list.next
                c2 = c2.next
               
        if carry!=0:
            sum_list.next = ListNode(carry)
        return a.next
                