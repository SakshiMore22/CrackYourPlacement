# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        dic={}
        q=[[root,0]]
        mi=float('inf')
        while q:
            for i in range(len(q)):
                node,lev=q.pop(0)
                if lev not in dic:
                    dic[lev]=node.val
                if node.right:
                    q.append([node.right,lev+1])
                if node.left:
                    q.append([node.left,lev+1])
        ans=[]
        # print(dic)
        for i in range(0,len(dic)):
            ans.append(dic[i])
        return ans
        