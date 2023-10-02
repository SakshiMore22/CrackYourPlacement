class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def calc(ind1,ind2):
            if ind1<0 and ind2<0:
                return True
            if ind2<0 and ind1>=0:
                return False
            if ind1<0 and ind2>=0:
                return all(c == '*' for c in p[:ind2+1])
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==p[ind2] or p[ind2]=='?': 
                dp[ind1][ind2]=calc(ind1-1,ind2-1)
                return dp[ind1][ind2]
            elif p[ind2]=='*':
                dp[ind1][ind2]=(calc(ind1,ind2-1) or calc(ind1-1,ind2))
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2]=False
                return dp[ind1][ind2]
        dp=[[-1 for i in range(len(p))] for j in range(len(s))]
        return calc(len(s)-1,len(p)-1)

        