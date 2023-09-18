from queue import PriorityQueue
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = PriorityQueue()
        for i in range(len(mat)):
            num=mat[i].count(1)
            q.put((num,i))
        ans=[]
        for i in range(k):
            ans.append(q.get()[1])
        #print(ans)
        return ans