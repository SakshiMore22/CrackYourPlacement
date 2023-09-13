class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        result = [1] * len(ratings)
        
        # left to right
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                result[i+1] = max(result[i+1], result[i] + 1)
        
        # right to left
        for i in reversed(range(0, len(ratings) - 1)):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1] + 1)
        
        
        return sum(result)