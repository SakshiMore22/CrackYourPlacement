class Solution:
    def numSplits(self, s: str) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        dic1={}
        cnt=0
        for i in range(1,len(s)):
            if s[i-1] in dic1:
                dic1[s[i-1]]+=1
            else:
                dic1[s[i-1]]=1
            if dic[s[i-1]]==1:
                del dic[s[i-1]]
            else:
                dic[s[i-1]]-=1
            if len(dic)==len(dic1):
                cnt+=1
        return cnt