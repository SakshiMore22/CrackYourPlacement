class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)] 
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        st=''
        i,j=len(text1),len(text2)
        while i>0 and j>0:
            if text1[i-1]==text2[j-1]:
                st+=text1[i-1]
                i-=1
                j-=1
            else:
                if dp[i-1][j]>=dp[i][j-1]:
                    st+=text1[i-1]
                    i-=1
                else:
                    st+=text2[j-1]
                    j-=1
        while i>0:
            st+=text1[i-1]
            i-=1
        while j>0:
            st+=text2[j-1]
            j-=1
        return st[::-1]
        