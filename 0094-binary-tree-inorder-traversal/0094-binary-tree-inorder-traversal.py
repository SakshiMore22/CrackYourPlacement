# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def ino(root,ans):
            if not root:
                return
            ino(root.left,ans)
            ans.append(root.val)
            ino(root.right,ans)
        ans=[]
        ino(root,ans)
        return ans