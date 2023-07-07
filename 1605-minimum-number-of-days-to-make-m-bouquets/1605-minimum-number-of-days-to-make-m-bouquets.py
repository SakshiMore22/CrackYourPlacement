class Solution:
    def poss(self,day,bl,m,k):
            flow,bouq=0,0
            for i in range(len(bl)):
                if bl[i]>day:
                    flow=0
                else:
                    flow+=1
                    if flow>=k:
                        bouq+=1
                        flow=0
            if flow>=k:
                bouq+=1 
            #print(day,bouq) 
            return bouq>=m
    def minDays(self, bl: List[int], m: int, k: int) -> int:
        if m*k>len(bl):
            return -1
    
        ans=-1
        l,r=0,10**9
        while l<=r:
            mid=(l+r)//2
            #print(mid)
            if self.poss(mid,bl,m,k):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        

