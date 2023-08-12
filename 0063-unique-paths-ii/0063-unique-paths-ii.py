class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def calc(r,c):
            if r==len(grid)-1 and c==len(grid[0])-1 :
                return int(grid[r][c]==0)
            if grid[r][c]==1:
                return 0
            if r>len(grid) and c>len(grid[0]):
                return 0
            if dp[r][c]!=-1:
                return dp[r][c]
            n_r,n_c=r+1,c+0
            pos1=0
            if n_r>=0 and n_r<len(grid) and n_c>=0 and n_c<len(grid[0]) and grid[n_r][n_c]==0:
                pos1=calc(n_r,n_c)
            n_r,n_c=r+0,c+1
            pos2=0
            if n_r>=0 and n_r<len(grid) and n_c>=0 and n_c<len(grid[0]) and grid[n_r][n_c]==0:
                pos2=calc(n_r,n_c)
            dp[r][c]=pos1+pos2
            return dp[r][c]
        dp=[[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        return calc(0,0)


                
                