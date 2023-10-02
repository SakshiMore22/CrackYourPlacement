class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(s)+1):
            dp[i][0]=False
        for i in range(1,len(p)+1):
            dp[0][i]=all(c == '*' for c in p[:i])
        for ind1 in range(1,len(s)+1):
            for ind2 in range(1,len(p)+1):
                if s[ind1-1]==p[ind2-1] or p[ind2-1]=='?': 
                    dp[ind1][ind2]=dp[ind1-1][ind2-1]
                elif p[ind2-1]=='*':
                    dp[ind1][ind2]=(dp[ind1][ind2-1] or dp[ind1-1][ind2])
                else:
                    dp[ind1][ind2]=False
        return dp[len(s)][len(p)]

        