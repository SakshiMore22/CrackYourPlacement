class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans=int(nums[0]!=0)
        nums.append(float('inf'))
        for i in range(len(nums)):
            if (i+1)>nums[i] and (i+1)<nums[i+1]:
                ans+=1
        return ans

        