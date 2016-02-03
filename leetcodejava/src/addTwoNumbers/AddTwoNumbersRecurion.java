package addTwoNumbers;

public class AddTwoNumbersRecurion {
	public ListNode addTwoNumbersRecurion(ListNode l1,ListNode l2){
		if(l1==null)
			return l2;
		if(l2==null)
			return l1;
		ListNode head=new ListNode(0);
		ListNode cur=head;
		int plus=0;
		while(l1!=null && l2!=null){
			int sum=l1.val+l2.val+plus;
			plus=sum/10;
			sum=sum%10;
			cur.next=new ListNode(sum);
			cur=cur.next;
			l1=l1.next;
			l2=l2.next;
		}
		if (l1!=null){
			if (plus!=0){
				cur.next=addTwoNumbersRecurion(l1,new ListNode(plus));
			}else{
				cur.next=l1;
			}
		}	
		else if (l2!=null){
				if (plus!=0){
					cur.next=addTwoNumbersRecurion(l2,new ListNode(plus));
				}else{
					cur.next=l2;
				}
		}else if(plus!=0){
			cur.next=new ListNode(plus);
		}
		return head.next;
	}
}
