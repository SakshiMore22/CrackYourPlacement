# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def calc(root):
            if root==None or root==p or root==q:
                return root
            lh=calc(root.left)
            rh=calc(root.right)
            if lh==None:
                return rh
            elif rh==None:
                return lh
            else:
                return root
        return calc(root)
            
            
        