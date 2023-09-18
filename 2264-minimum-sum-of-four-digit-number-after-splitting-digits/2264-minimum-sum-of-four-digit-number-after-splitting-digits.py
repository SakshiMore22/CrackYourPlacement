class Solution:
    def minimumSum(self, num: int) -> int:
        ans=[]
        for i in str(num):
            if i!='0':
                ans.append(int(i))
        ans.sort()
        c1,c2=0,0
        for i in range(len(ans)):
            if i%2==0:
                c1=c1*10+ans[i]
            else:
                c2=c2*10+ans[i]
            # print(c1,c2)
        return c1+c2
        