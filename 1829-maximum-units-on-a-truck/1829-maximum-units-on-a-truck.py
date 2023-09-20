class Solution:
    def maximumUnits(self, box: List[List[int]], t: int) -> int:
        new=sorted(box, key=lambda x: -x[1])
        print(new)
        cnt,j=0,0
        while t and j<len(new):
            if new[j][0]<=t:
                t-=new[j][0]
                cnt+=(new[j][1]*new[j][0])
            else:
                cnt+=(t*new[j][1])
                t=0
            j+=1
        return cnt
            
        