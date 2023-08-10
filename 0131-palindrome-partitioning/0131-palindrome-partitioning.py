class Solution:
    def partition(self, s):
        def palindrome(a):
            return a == a[::-1]
        def calc(ind,ans):
            if ind==len(s):
                res.append(ans[:])
                return
            for i in range(ind,len(s)):
                temp=s[ind:i+1]
                if palindrome(temp):
                    calc(i+1,ans+[temp])
            return

        res=[]
        calc(0,[])
        return res