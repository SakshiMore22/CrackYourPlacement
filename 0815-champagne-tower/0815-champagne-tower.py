class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def calc(cap,r,c):
            if r==query_row and c==query_glass:
                return cap
            if r>query_row or c>query_glass or query_glass>query_row:
                return 0.00
            # if cap<0:
            #     return 0.0
            if dp[r][c]!=-1:
                return dp[r][c]
            lef=(calc(cap,r+1,c)-1)/2.0
            rig=(calc(cap,r+1,c+1)-1)/2.0
            if lef<0:
                lef=0
            if rig<0:
                rig=0
            dp[r][c]=lef+rig
            return dp[r][c]
        dp=[[-1 for i in range(101)] for j in range(101)]
        return min(1.0,calc(poured,0,0))


        
        
        