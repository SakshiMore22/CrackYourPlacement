# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q=deque([root])
        dic={}
        while q:
            n=len(q)
            for i in range(n):
                node=q.pop()
                if node.val==target:
                    Target=node
                if node.left:
                    q.append(node.left)
                    dic[node.left]=node
                if node.right:
                    q.append(node.right)
                    dic[node.right]=node
        c=0
        vis=[]
        ans=[target]
        while c<k:
            for i in range(len(ans)):
                tar=ans.pop(0)
                vis.append(tar)
                if tar.left and tar.left not in vis:
                    ans.append(tar.left)
                    vis.append(tar.left)
                if tar.right and tar.right not in vis:
                    ans.append(tar.right)
                    vis.append(tar.right)
                if dic.get(tar)!=None and dic[tar] not in vis:
                    ans.append(dic[tar])
                    vis.append(dic[tar])
            c+=1
        print(ans)
        fin=[]
        while ans:
            fin.append(ans.pop(0).val)
        return fin