class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        vis=set()
        q=deque([])
        mat1=[[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    vis.add((i,j))
        while q:
            r,c,cnt=q.popleft()
            for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
                if (r+i)>=0 and (r+i)<len(mat) and (c+j)>=0 and (c+j)<len(mat[0]) and (r+i,c+j) not in vis:
                    q.append((r+i,c+j,cnt+1))
                    mat1[r+i][c+j]=cnt+1
                    vis.add((r+i,c+j))


        return mat1
