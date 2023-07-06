# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], K: int) -> Optional[ListNode]:
        if K==0:
            return head
        temp=head
        cnt=0
        while temp:
            temp=temp.next
            cnt+=1
        if cnt==0:
            return
        start=head
        K=K%cnt
        k=(cnt-K)-1
        while k:
            head=head.next
            k-=1
        temp1=head
        while head.next:
            head=head.next
        head.next=start
        ans=temp1.next
        temp1.next=None
        return ans
