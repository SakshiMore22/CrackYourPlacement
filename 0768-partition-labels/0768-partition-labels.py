class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i in range(len(s)):
            dic[s[i]]=i
        prev=-1
        maxi=0
        ans=[]
        for i in range(len(s)):
            maxi=max(maxi,dic[s[i]])
            if maxi==i:
                ans.append(maxi-prev)
                prev=maxi
        return ans

        