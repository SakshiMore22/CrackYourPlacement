class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)//3
        ans=set()
        for i in range(len(nums)):
            if i==0:
                c=1
                if c>n :
                    ans.add(nums[0])
            elif nums[i]==nums[i-1]:
                c+=1
                if c>n:
                    ans.add(nums[i])
            else:
                c=1
                if c>n:
                    ans.add(nums[i]) 
        return list(ans)
        