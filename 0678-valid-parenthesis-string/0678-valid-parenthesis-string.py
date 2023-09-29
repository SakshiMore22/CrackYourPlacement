class Solution:
    def checkValidString(self, s: str) -> bool:
        dp=[[False for i in range(len(s)+1)]for j in range(len(s)+1)]
        dp[len(s)][0]=True
        for ind in range(len(s)-1,-1,-1):
            for op in range(len(s)):
                ans=False
                if s[ind]=='(':
                    ans=ans or dp[ind+1][op+1]
                elif s[ind]==')':
                    if op:
                        ans=ans or dp[ind+1][op-1]
                else:
                    ans=ans or dp[ind+1][op+1]
                    if op:
                        ans=ans or dp[ind+1][op-1]
                    ans=ans or dp[ind+1][op]
                dp[ind][op]=ans
        return dp[0][0]

        
        