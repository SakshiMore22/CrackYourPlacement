# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc(node):
            if node==None:
                return 0
            lh=calc(node.left)
            if lh==-1:
                return -1
            rh=calc(node.right)
            if rh==-1:
                return -1
            if abs(lh-rh)>1:
                return -1
            return 1+max(lh,rh)
        if calc(root)==-1:
            return False
        return True
        