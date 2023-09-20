class Solution:
	def coinChange(self, coins, V):
	    def calc(V,ind):
	        if ind>=len(coins) or V<=0:
	            if V==0:
	                return 0
	            else:
	                return float('inf')
	        if dp[ind][V]!=-1:
	            return dp[ind][V]
	        pi=float('inf')
	        if coins[ind]<=V:
	            pi=1+calc(V-coins[ind],ind)
	        npi=0+calc(V,ind+1)
	        dp[ind][V]=min(pi,npi)
	        return dp[ind][V]
	    dp=[[-1 for i in range(V+1)] for j in range(len(coins))]
	    ans=calc(V,0)
	    if ans==float('inf'):
	        return -1
	    return ans