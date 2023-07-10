# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        temp=head.next.next
        st=head.next
        ev,od=head,head.next
        cnt=2
        while temp:
            if cnt%2==0:
                ev.next=temp
                ev=ev.next
            else:
                od.next=temp
                od=od.next
            temp=temp.next
            cnt+=1
        ev.next=st
        od.next=None
        return head
            



        