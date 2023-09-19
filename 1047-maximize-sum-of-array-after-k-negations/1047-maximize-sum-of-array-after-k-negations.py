class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        temp=nums
        print(nums,temp)
        s=0
        for i in range(len(nums)):
            if temp[i]<0 and k>0:
                nums[i]=-nums[i]
                k-=1
            else:
                break
        # print(s,i)
        if k>0:
            if k%2==1:
                if i==0:
                    nums[i]=-nums[i]
                else:
                    if abs(temp[i-1])<temp[i]:
                        nums[i-1]=-nums[i-1]
                    else:
                        nums[i]=-nums[i]
        # print(nums)
        return sum(nums)