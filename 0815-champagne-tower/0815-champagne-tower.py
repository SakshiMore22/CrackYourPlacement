class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#stupid test
        if poured == 0: return 0
#defenition of the size of rectangles
        n = query_row-query_glass+1
        m = query_glass+1
        n, m = max(n,m), min(n,m)
#defifnition of value in the first column of rectangle
        dp = [0]*n
        dp[0] = poured
        for i in range(n-1): dp[i+1] = max((dp[i]-1)/2,0)
#evolution of column of rectangle
        for j in range(1,m):
            for i in range(n):
                if i == 0: dp[i] = max((dp[i]-1)/2,0)
                else:  dp[i] = max((dp[i]-1)/2,0) + max((dp[i-1]-1)/2,0)
        return min(dp[-1],1)

            





            
            
        
        