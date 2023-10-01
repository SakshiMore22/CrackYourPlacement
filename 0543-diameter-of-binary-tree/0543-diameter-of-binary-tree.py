# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calc(root):
            if root==None:
                return 0
            lh=calc(root.left)
            rh=calc(root.right)
            self.maxi=max(self.maxi,(lh+rh))
            return 1+max(lh,rh)
        self.maxi=0
        calc(root)
        return self.maxi

        