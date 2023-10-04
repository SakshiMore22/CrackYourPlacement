# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        q=deque([(root, 0)])
        ma=0
        while q:
            _,st=q[0]
            for i in range(len(q)):
                node,val= q.popleft()
                if node.left:
                    q.append((node.left,val*2))
                if node.right:
                    q.append((node.right,val*2+1))
                ma=max(ma,(val-st)+1)
        return ma
        