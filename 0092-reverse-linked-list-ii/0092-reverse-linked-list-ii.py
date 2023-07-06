# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], lef: int, righ: int) -> Optional[ListNode]:
        if lef==righ:
            return head
        temp1,temp=head,head
        cnt=1
        ini=None
        while temp :
            if cnt==lef-1:
                ini=temp
            if cnt==lef:
                left=temp
            if cnt==righ:
                right=temp
            temp=temp.next
            cnt+=1
        temp=head
        st,prev=left,left
        left=left.next
        while prev!=right:
            nex=left.next
            left.next=prev
            prev=left
            left=nex
        st.next=left
        if ini:
            ini.next=right
            return temp
        return prev