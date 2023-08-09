class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def calc(ind,temp):
            ans.append(temp[:])
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                calc(i+1,temp)
                temp.pop()
        ans=[]
        nums.sort()
        calc(0,[])
        return ans