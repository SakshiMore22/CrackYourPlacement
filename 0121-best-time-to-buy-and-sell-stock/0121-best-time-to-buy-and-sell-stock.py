class Solution:
    def maxProfit(self, pri: List[int]) -> int:
        pre=[]
        mi=pri[-1]
        for i in range(len(pri)-1,-1,-1):
            pre.append(mi)
            mi=max(mi,pri[i])
        pre=pre[::-1]
        ma=float('-inf')
        for i in range(len(pri)):
            ma=max(ma,pre[i]-pri[i])
        return ma

        