# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic={}
        for i in range(len(inorder)):
            dic[inorder[i]]=i
        def calc(in1,in2,pre1,pre2):
            if in1>in2 or pre1>pre2:
                return None
            root=TreeNode(preorder[pre1])
            i1=dic[root.val]
            num=i1-in1
            root.left=calc(in1,i1-1,pre1+1,pre1+num)
            root.right=calc(i1+1,in2,pre1+num+1,pre2)
            return root
        return calc(0,len(inorder)-1,0,len(preorder)-1)


        