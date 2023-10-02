from collections import Counter
class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        def calc(ind1,ind2):
            if ind2<0:
                return ind1+1
            if ind1<0:
                return ind2+1
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2]=0+calc(ind1-1,ind2-1)
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2]=min(1+calc(ind1-1,ind2-1),1+calc(ind1-1,ind2),1+calc(ind1,ind2-1))
                return dp[ind1][ind2]
        dp=[[-1 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        return calc(len(text1)-1,len(text2)-1)