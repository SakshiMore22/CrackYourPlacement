import numpy as np
class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        dic={}
        for i in range(len(gs)):
            if gs[i] in dic:
                dic[gs[i]].append(i)
            else:
                dic[gs[i]]=[i]
        ans=[]
        for i in dic:
            for j in range(0, len(dic[i]), i): 
                ans.append(dic[i][j:j + i])
        return ans