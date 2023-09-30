from queue import PriorityQueue
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        q = PriorityQueue()
        for i in range(len(nums2)):
            q.put((-nums2[i],i))
        nums1.sort()
        i,j=0,len(nums1)-1
        ans=[-1 for i in range(len(nums1))]
        while not q.empty():
            num=q.get()
            if nums1[j]>(-num[0]):
                ans[num[1]]=nums1[j]
                j-=1
            else:
                ans[num[1]]=nums1[i]
                i+=1
        return ans