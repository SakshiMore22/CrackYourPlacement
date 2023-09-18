class Solution:
    def distMoney(self, mo: int, ch: int) -> int:
        if mo<ch:
            return -1
        cnt=0
        mo-=ch
        for i in range(ch):
            if mo>=7 :
                if (mo-7)!=3 or (ch-i-1)>1:
                    cnt+=1
                    mo-=7
                else:
                    mo=0
            else:
                mo=0
            print(cnt,mo)
        if mo>0:
            cnt-=1
        return cnt

        