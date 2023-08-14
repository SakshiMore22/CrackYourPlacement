from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:  
        q = PriorityQueue()
        for i in nums:
            q.put(-i)
        while k>1:
            q.get()
            k-=1
        return -(q.get())