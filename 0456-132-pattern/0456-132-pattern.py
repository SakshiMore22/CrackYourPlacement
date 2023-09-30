class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            if not stack or num < stack[-1][0]:
                stack.append([num, num]) 
            else:
                mini = stack[-1][0]
                while stack and stack[-1][1] < num:
                    stack.pop()
                if stack and stack[-1][0] < num and stack[-1][1] > num:
                    return True
                else:
                    stack.append([mini, num])
        return False
            
