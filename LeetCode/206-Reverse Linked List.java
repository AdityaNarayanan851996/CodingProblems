// 			206. Reverse Linked List
// 			https://leetcode.com/problems/reverse-linked-list/description/
//code
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode curr = head;
        ListNode nxt = curr.next;
        curr.next = null;
        while(nxt != null){ 
                ListNode tmp = nxt.next;
                nxt.next = curr;
                curr = nxt;
                nxt = tmp;
        }
        return curr;
    }
}