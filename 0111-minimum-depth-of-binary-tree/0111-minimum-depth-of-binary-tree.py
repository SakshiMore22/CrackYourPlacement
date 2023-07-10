# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        q=[[root,1]]
        ans=float('inf')
        while q:
            for i in range(len(q)):
                temp=q.pop(0)
                nod=temp[0]
                cnt=temp[1]
                if not nod.left and not nod.right:
                    print(ans)
                    ans=min(ans,cnt)
                    return ans
                if nod.left:
                    q.append([nod.left,cnt+1])
                if nod.right:
                    q.append([nod.right,cnt+1])
        return ans
                
