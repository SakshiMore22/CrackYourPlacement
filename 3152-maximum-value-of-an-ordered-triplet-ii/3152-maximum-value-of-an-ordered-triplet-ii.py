class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mi=[nums[0]]
        for i in range(1,len(nums)):
            mi.append(max(mi[-1],nums[i]))
        ma=[-1 for i in range(len(nums))]
        ma[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            ma[i]=max(ma[i+1],nums[i])
        ans=0
        for i in range(1,len(nums)-1):
            ans=max(ans,(mi[i-1]-nums[i])*ma[i+1])
        return ans

