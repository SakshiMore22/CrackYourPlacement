class Solution:
    def checkValidString(self, s: str) -> bool:
        def calc(ind,op):
            if ind==len(s):
                return op==0
            if dp[ind][op]!=-1:
                return dp[ind][op]
            ans=False
            if s[ind]=='(':
                ans=ans or calc(ind+1,op+1)
            elif s[ind]==')':
                if op:
                    ans=ans or calc(ind+1,op-1)
            else:
                ans=ans or calc(ind+1,op+1)
                if op:
                    ans=ans or calc(ind+1,op-1)
                ans=ans or calc(ind+1,op)
            dp[ind][op]=ans
            return dp[ind][op]
        dp=[[-1 for i in range(len(s))]for j in range(len(s))]
        return calc(0,0)

        