# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        slow1=headA
        slow2=headB
        while slow1!=slow2:
            if slow1 is None:
                slow1=headB  
            else:
                slow1=slow1.next
            if slow2 is None:
                slow2=headA 
            else:
                slow2=slow2.next
    
        return slow2
    
        
            
        