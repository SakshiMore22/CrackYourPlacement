class Solution:
    def minSubArrayLen(self, s, nums):
        total = left = right = 0
        res=len(nums)+1
        if sum(nums)<s:
            return 0
        while right < len(nums):
            total += nums[right]
            print(total)
            while total >= s:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return res 


