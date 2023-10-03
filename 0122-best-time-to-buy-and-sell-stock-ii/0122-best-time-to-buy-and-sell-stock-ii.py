class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def calc(ind,bu):
            if ind>=len(prices) :
                return 0
            if dp[ind][bu]!=-1:
                return dp[ind][bu]
            if bu==0:
                dp[ind][bu]=max(-prices[ind]+calc(ind+1,1),0+calc(ind+1,0))
                return dp[ind][bu]
            if bu==1:
                dp[ind][bu]=max(prices[ind]+calc(ind+1,0),0+calc(ind+1,1))
                return dp[ind][bu]
        dp=[[ -1 for j in range(2)] for k in range(len(prices))]
        return calc(0,0)
        