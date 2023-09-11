class Solution:
    def rob(self, nums: List[int]) -> int:
        def calc(ind):
            if ind==0:
                return nums[ind]
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            lst1=calc(ind-1)
            lst=nums[ind]+calc(ind-2)
            dp[ind]=max(lst,lst1)
            return dp[ind]
        dp=[-1 for i in range(len(nums))]
        return calc(len(nums)-1)
        