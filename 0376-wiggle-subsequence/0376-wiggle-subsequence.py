class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        c=0
        stat=None
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and stat!=True:
                stat=True
                c+=1
            if nums[i]<nums[i-1] and stat!=False:
                stat=False
                c+=1
        return c+1