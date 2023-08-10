class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums[0]==target:
            return True
        elif nums[0]<target:
            i=1
            while i<len(nums) and nums[i]<=target:
                if nums[i]==target:
                    return True
                i+=1
            return False
        else:
            i=len(nums)-1
            while i>0 and nums[i]>=target:
                if nums[i]==target:
                    return True
                i-=1
            return False
