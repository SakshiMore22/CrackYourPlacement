class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]<nums[1]:
            return sorted(nums)==nums
        elif  nums[0]==nums[1]:
            return sorted(nums,reverse=True)==nums or sorted(nums)==nums
        else:
            return sorted(nums,reverse=True)==nums
        