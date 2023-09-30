class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        di={}
        i,j=0,0
        ans=[]
        while j<len(s):
            if s[j] in di:
                di[s[j]]+=1
            else:
                if len(di)>0:
                    c=0
                    for k in di:
                        if dic[k]==di[k]:
                            c+=1
                    if c==len(di):
                        ans.append(j-i)
                        di={s[j]:1}
                        i=j
                    else:
                        di[s[j]]=1
                else:
                    di[s[j]]=1
                
            j+=1
            # print(di)
        if len(di)>0:
            ans.append(j-i)
        return ans



        