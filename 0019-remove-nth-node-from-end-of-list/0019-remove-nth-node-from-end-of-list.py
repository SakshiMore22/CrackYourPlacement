# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return None
        cnt=0
        temp=head
        while temp:
            cnt+=1
            temp=temp.next
        if cnt==1:
            return None
        if cnt==n:
            return head.next
        rem=cnt-n
        temp=head
        c=0
        while c<rem-1:
            c+=1
            temp=temp.next
        #print(temp.val)
        temp.next=temp.next.next
        return head
