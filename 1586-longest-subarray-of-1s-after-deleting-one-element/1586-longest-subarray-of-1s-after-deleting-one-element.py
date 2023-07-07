class Solution:
    def longestSubarray(self, an):
        if len(an)==1 :
            return 0
        l,r=0,0
        k=1
        ans=0
        while r<len(an):
            if an[r]==0:
                k-=1
            if k>=0:
                ans=max(ans,r-l)
            if k<0:
                while k<0:
                    if an[l]==0:
                        k+=1
                    l+=1
            #print(l,r,ans,k)
            r+=1
        #print(ans)
        return ans