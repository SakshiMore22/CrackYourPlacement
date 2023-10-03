class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def calc(ind,bu,cnt):
            if ind==len(prices) or cnt==2:
                return 0
            if dp[ind][bu][cnt]!=-1:
                return dp[ind][bu][cnt]
            if bu==0:
                dp[ind][bu][cnt]=max(-prices[ind]+calc(ind+1,1,cnt),0+calc(ind+1,0,cnt))
                return dp[ind][bu][cnt]
            else:
                dp[ind][bu][cnt]=max(prices[ind]+calc(ind+1,0,cnt+1),0+calc(ind+1,1,cnt))
                return dp[ind][bu][cnt] 
        dp=[[[-1 for i in range(3)] for j in range(2)] for k in range(len(prices))]
        return calc(0,0,0)




        