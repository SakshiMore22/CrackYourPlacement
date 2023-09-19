class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)<3:
            return True
        cnt=0
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                temp1 = s[0:i] + s[i+1:]
                temp2 = s[0:j] + s[j+1:]
                if temp1 == temp1[::-1]: return True
                elif temp2 == temp2[::-1]: return True
                else:
                    return False
            else:
                i+=1
                j-=1
        return True

        

        