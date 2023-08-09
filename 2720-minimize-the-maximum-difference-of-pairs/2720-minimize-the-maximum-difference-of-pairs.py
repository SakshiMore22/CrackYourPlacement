class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        le,ri=0,nums[-1]-nums[0]
        while le<=ri:
            mid=(le+ri)//2
            i,cnt=1,0
            while i<len(nums):
                if (nums[i]-nums[i-1])<=mid:
                    cnt+=1
                    i+=2
                else:
                    i+=1
            if cnt>=p:
                ri=mid-1
            else:
                le=mid+1
        return le

        