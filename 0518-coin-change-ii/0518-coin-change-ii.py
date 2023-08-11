class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def calc(s,ind):
            if s==0:
                return 1
            if ind==len(coins):
                return 0
            if dp[s][ind]!=-1:
                return dp[s][ind]
            n=calc(s,ind+1)
            y=0
            if s>=coins[ind]:
                y=calc(s-coins[ind],ind)
            dp[s][ind]=n+y
            return dp[s][ind]
        dp=[[-1 for i in range(len(coins))] for j in range(amount+1)]
        return calc(amount,0)
            