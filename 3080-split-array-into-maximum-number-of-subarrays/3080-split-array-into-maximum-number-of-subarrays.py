class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        ans=0
        cur=-1
        prev=0
        for i in range(len(nums)):
            if cur==-1:
                prev=nums[i]
                cur=1
            else:
                prev=prev&nums[i]
            if prev==0:
                ans+=1
                cur=-1
            # print(prev,cur)
        if ans==0:
            return 1
        else:
            return ans

            
        
        