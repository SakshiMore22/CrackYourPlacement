class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i,j=0,0
        s=0
        tot=sum(nums)
        if tot<x:
            return -1
        ans=float('inf')
        while j<len(nums) :
            s+=nums[j]
            if (tot-s)==x:
                ans=min(ans,len(nums)-(j-i+1))
                j+=1
            elif (tot-s)>x:
                j+=1
            else:
                while i<len(nums) and (tot-s)<x:
                    s-=nums[i]
                    i+=1
                if (tot-s)==x:
                    ans=min(ans,len(nums)-(j-i+1))
                j+=1
            print(ans,i,j)
        if ans==float('inf'):
            return -1
        else:
            return ans
            

