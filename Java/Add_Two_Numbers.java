/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode p = head;
        int r, q = 0;
        while(l1 != null || l2 != null){
            r = q;
            if(l1 != null){
                r += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                r += l2.val;
                l2 = l2.next;
            }   
            q = r / 10;
            r = r % 10;
            p.next = new ListNode(r);
            p = p.next;
        }

        
        if(q == 1){
            p.next = new ListNode(1);
        }

        return head.next;        
    }
}