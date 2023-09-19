class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j=0,0
        cnt=0
        while i<len(s) and j<len(g):
            # print(s[i],g[i],i,j)
            if s[i]>=g[j]:
                cnt+=1
                i+=1
                j+=1
            else:
                i+=1
        return cnt