class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        c=0
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                c+=dic[i]
                dic[i]+=1
        return c

        