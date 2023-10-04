# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q=[root]
        dic={}
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                if node.left:
                    dic[node.left]=node
                    q.append(node.left)
                if node.right:
                    dic[node.right]=node
                    q.append(node.right)
        q=[target]
        ans=[]
        vis=[target]
        c=0
        while q:
            if c==k:
                break
            c+=1
            for i in range(len(q)):
                node=q.pop(0)
                if node.left and (node.left) not in vis:
                    q.append(node.left)
                    vis.append(node.left)
                if node.right and node.right not in vis:
                    q.append(node.right)
                    vis.append(node.right)
                if node in dic and dic[node] not in vis:
                    q.append(dic[node])
                    vis.append(dic[node])
        while q:
            i=q.pop(0)
            ans.append(i.val)
        return ans
                
        