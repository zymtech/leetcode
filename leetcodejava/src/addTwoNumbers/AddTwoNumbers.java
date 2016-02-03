package addTwoNumbers;
/*You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/
public class AddTwoNumbers {
	public ListNode addTwoNumbers(ListNode l1,ListNode l2){
		ListNode r=new ListNode(0);
		ListNode h=r;
		ListNode beforeend=r;
		
		while(l1!=null && l2!=null){
			r.val+=l1.val+l2.val;
			r.next=new ListNode(r.val/10);
			r.val%=10;
			
			beforeend=r;
			r=r.next;
			l1=l1.next;
			l2=l2.next;
		}
		
		ListNode rest;
		if (l1==null) 
			rest=l2;
		else
			rest=l1;
		
		while(rest!=null){
			r.val+=rest.val;
			r.next=new ListNode(r.val/10);
			r.val%=10;
			
			beforeend=r;
			r=r.next;
			rest=rest.next;
		}
		if(beforeend.next!=null && beforeend.next.val==0) 
			beforeend.next=null;
		
		return h;
	}
}
