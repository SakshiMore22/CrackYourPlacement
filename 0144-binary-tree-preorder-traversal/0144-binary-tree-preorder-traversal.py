
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def calc(root,ans):
            if not root:
                return 
            ans.append(root.val)
            # print(ans)
            calc(root.left,ans)
            calc(root.right,ans)
            # return ans
        ans=[]
        calc(root,ans)
        return ans
