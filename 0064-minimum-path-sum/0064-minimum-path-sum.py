class Solution:
    def minPathSum(self, grid):
        def calc(r,c):
            if r==len(grid)-1 and c==len(grid[0])-1:
                return grid[r][c]
            if r>len(grid) and c>len(grid[0]):
                return float('inf')
            if dp[r][c]!=-1:
                return dp[r][c]
            c1=float('inf')
            if r+1>=0 and r+1<len(grid):
                c1=grid[r][c]+calc(r+1,c)
            c2=float('inf')
            if c+1>=0 and c+1<len(grid[0]):
                c2=grid[r][c]+calc(r,c+1)
            dp[r][c]=min(c1,c2)
            return  dp[r][c]
        dp=[[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        return calc(0,0)

