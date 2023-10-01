# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic={}
        q=[[root,0,0]]
        mi=float('inf')
        while q:
            for i in range(len(q)):
                node,ind,lev=q.pop(0)
                if ind not in dic:
                    dic[ind]={lev:[node.val]}
                    mi=min(mi,ind)
                else:
                    if lev in dic[ind]:
                        dic[ind][lev].append(node.val)
                    else:
                        dic[ind][lev]=[node.val]
                if node.right:
                    q.append([node.right,ind+1,lev+1])
                if node.left:
                    q.append([node.left,ind-1,lev+1])
        ans=[]
        # print(dic)
        for i in range(mi,mi+len(dic)):
            dic1=dic[i]
            lev=[]
            for i in dic1:
                if len(dic1[i])>1:
                    lev+=sorted(dic1[i])
                else:
                    lev+=dic1[i]
            ans.append(lev)
        return ans