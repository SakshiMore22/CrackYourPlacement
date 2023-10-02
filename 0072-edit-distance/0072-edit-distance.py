from collections import Counter
class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for i in range(len(text1)+1):
            dp[i][0]=i
        for i in range(len(text2)+1):
            dp[0][i]=i
        for ind1 in range(1,len(text1)+1):
            for ind2 in range(1,len(text2)+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=0+dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=min(1+dp[ind1-1][ind2-1],1+dp[ind1-1][ind2],1+dp[ind1][ind2-1])
        return dp[len(text1)][len(text2)]