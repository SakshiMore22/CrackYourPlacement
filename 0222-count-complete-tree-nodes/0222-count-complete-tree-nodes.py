# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def calc(root):
            if root==None:
                return 0
            return calc(root.left)+calc(root.right)+1
        return calc(root)
        