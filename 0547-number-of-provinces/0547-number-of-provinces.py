class Solution:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()
        def dfs(node):
            seen.add(node)
            for i,j in enumerate(A[node]):
                if j and i not in seen:
                    seen.add(i)
                    dfs(i)

        
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans