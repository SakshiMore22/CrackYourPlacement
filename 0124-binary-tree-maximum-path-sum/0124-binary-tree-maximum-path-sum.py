# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def calc(root):
            if root==None:
                return 0
            lh=max(0,calc(root.left))
            rh=max(0,calc(root.right))
            self.maxi=max(self.maxi,rh+lh+root.val)
            return max(rh,lh)+root.val
        self.maxi=float('-inf')
        calc(root)
        return self.maxi


        