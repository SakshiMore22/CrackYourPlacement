class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        ans=[[1],[1,1]]
        for i in range(2,n):
            top=ans[-1]
            temp=[1]
            for j in range(1,len(top)):
                temp.append(top[j]+top[j-1])
            temp.append(1)
            ans.append(temp)
        return ans
