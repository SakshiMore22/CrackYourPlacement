class Solution:
    def reverseWords(self, s: str) -> str:
        st=""
        for i in s.split():
            st+=i[::-1]
            st+=" "
        return st[:-1]
        