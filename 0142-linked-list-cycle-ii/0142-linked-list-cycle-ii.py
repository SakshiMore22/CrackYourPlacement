# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        if head==None or pos==-1:
            return None
        while head:
            if head in lst:
                return head
            else:
                lst.append(head)
                head=head.next
        return None