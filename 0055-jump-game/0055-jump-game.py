class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ma=0
        for i in range(len(nums)):
            if ma<i:
                return False
            ma=max(ma,i+nums[i])
        return ma>=len(nums)-1



        


        