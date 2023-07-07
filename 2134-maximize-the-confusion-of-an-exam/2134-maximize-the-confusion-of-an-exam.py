class Solution:
    def maxConsecutiveAnswers(self, an: str, K: int) -> int:
        if K>=len(an):
            return len(an)
        l,r=0,0
        k=K
        ans=float('-inf')
        while r<len(an):
            if an[r]=='F':
                k-=1
            if k>=0:
                ans=max(ans,r-l+1)
            if k<0:
                while k<0:
                    if an[l]=='F':
                        k+=1
                    l+=1
            # print(l,r,ans,k)
            r+=1
        k=K
        l,r=0,0
        while r<len(an):
            if an[r]=='T':
                k-=1
            #print(k,l,r)
            if k>=0:
                ans=max(ans,r-l+1)
            if k<0:
                while k<0 and l<len(an):
                    if an[l]=='T':
                        k+=1
                    l+=1
            #print(l,r,ans,k)
            r+=1
        print(ans)
        return ans
