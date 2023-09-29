class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num=str(num)
        if len(num)==k:
            return "0"
        stk=[]
        for i in range(len(num)):
            while stk and k and stk[-1]>int(num[i]):
                stk.pop()
                k-=1
            stk.append(int(num[i]))
        if k>0:
            stk=stk[:len(stk)-k]
        f=0
        st=''
        for i in range(len(stk)):
            if stk[i]>0:
                f=1
            if f==1:
                st+=str(stk[i])
        return st if len(st)>0 else "0"

        