# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def calc(root,s,li):
            if root==None:
                return
            li.append(root.val)
            s-=root.val
            if root.left==None and root.right==None and s==0:
                self.ans.append(li[:])
            if root.left:
                calc(root.left,s,li)
            if root.right:
                calc(root.right,s,li)
            s+=root.val
            li.pop()
        self.ans=[]
        calc(root,targetSum,[])
        return self.ans
        