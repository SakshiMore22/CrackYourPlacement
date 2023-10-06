class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot=[]
        fr=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rot.append([i,j])
                if grid[i][j]==1:
                    fr+=1
        cnt=0
        print(fr)
        while rot and fr>0:
            cnt=cnt+1
            for _ in range(len(rot)):
                r,c=rot.pop(0)
                for nr,nc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = r+nr, c+nc
                    if xx<0 or xx==len(grid) or yy<0 or yy==len(grid[0]):
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    grid[xx][yy]=2
                    rot.append((xx,yy))
                    fr-=1
        if fr==0:
            return cnt
        return -1


        