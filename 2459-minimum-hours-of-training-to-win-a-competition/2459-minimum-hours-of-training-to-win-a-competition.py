class Solution:
    def minNumberOfHours(self, en: int, ex: int, ene: List[int], exp: List[int]) -> int:
        cnt=(sum(ene)-en)+1
        if cnt<0:
            cnt=0
        for i in range(len(ene)):
            if ex<=exp[i]:
                cnt+=abs(ex-exp[i])+1
                ex+=abs(ex-exp[i])+1
            ex+=exp[i]
            # print(cnt,ex)
        return cnt

        