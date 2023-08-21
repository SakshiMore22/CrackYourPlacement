class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i=1
        while i<=len(s)//2:
            sub=s[:i]
            n=len(s)//len(sub)
            #print(sub,n)
            if s==sub*n:
                return True
            i+=1
        return False
