class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans=0
        i=0
        while i<len(nums):
            if nums[i]%2==0 and  nums[i]<=threshold:
                l,r=i,i
                f=0
                while True and r<len(nums):
                    if f==1 and nums[r]%2==1 and nums[r]<=threshold:
                        ans=max(ans,r-l+1)
                        r+=1
                        f-=1
                    elif f==0 and nums[r]%2==0 and nums[r]<=threshold:
                        ans=max(ans,r-l+1)
                        r+=1
                        f+=1
                    else:
                        break
                    # print(l,r)
                i+=1
            else:
                i+=1
        return ans