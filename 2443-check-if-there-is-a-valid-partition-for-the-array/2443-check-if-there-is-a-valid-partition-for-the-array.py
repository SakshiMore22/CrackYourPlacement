class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def calc(i):
            #print(i)
            if i>=len(nums):
                return True
            if dp[i]!=-1:
                return dp[i]
            two=False
            if i+1<len(nums):
                two=nums[i]==nums[i+1]
            thre1=False
            if i+2<len(nums):
                thre1=nums[i]==nums[i+1]==nums[i+2]
            thre=False
            if i+2<len(nums):
                thre=nums[i+2]==nums[i+1]+1==nums[i]+2
            #print(two,thre1,thre)
            dp[i]=(two and calc(i+2)) or (thre and calc(i+3)) or (thre1 and calc(i+3))
            return dp[i]
        dp=[-1 for i in range(len(nums))]
        return calc(0)