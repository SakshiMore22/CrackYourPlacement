class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def calc(ind1,ind2):
            if ind1<0:
                return int(ind2<0)
            if ind2<0:
                return 1
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==t[ind2]:
                dp[ind1][ind2]=(calc(ind1-1,ind2-1)+calc(ind1-1,ind2))
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2]=calc(ind1-1,ind2)
                return dp[ind1][ind2]
        dp=[[-1 for i in range(len(t))] for j in range(len(s))]
        return calc(len(s)-1,len(t)-1)