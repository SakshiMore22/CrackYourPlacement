class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        ind=0
        fu=0
        for i in range(len(gas)):
            fu+=gas[i]
            fu-=cost[i]
            if fu<0:
                ind=i+1
                fu=0
        return ind

        # return ans
        