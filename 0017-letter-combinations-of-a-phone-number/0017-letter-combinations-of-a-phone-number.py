class Solution:
    def letterCombinations(self, digit: str) -> List[str]:
        def helper(ind,st):
            if ind==len(digit):
                ans.append("".join(st))
                return
            for i in arr[int(digit[ind])]:
                st.append(i)
                # print(st)
                helper(ind+1,st)
                st.pop()
        ans=[]
        arr=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digit)==0:
            return []
        helper(0,[])
        return ans