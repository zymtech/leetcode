package linkedList;


import java.util.HashSet;
import java.util.Set;

/**
 * Created by Administrator on 9/29/2016.
 */

public class LinkedListCycle {
    public boolean hasCycle(ListNode head){
        Set<ListNode> nodeSeen = new HashSet<ListNode>();
        while (head != null){
            if (nodeSeen.contains(head)){
                return true;
            }
            else{
                nodeSeen.add(head);
            }
            head = head.next;
        }
        return false;
    }
    public static void main(String[] args){
        LinkedListCycle test = new LinkedListCycle();
        ListNode head = new ListNode(5);
        ListNode dummy;
        dummy = head;
        head.next = new ListNode(4);
        head.next.next = new ListNode(3);
        head.next.next.next = dummy;
        System.out.println(test.hasCycle(head));
    }
}
