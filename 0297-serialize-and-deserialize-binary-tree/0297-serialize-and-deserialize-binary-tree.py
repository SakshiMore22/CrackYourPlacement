# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        if root==None:
            return ''
        st=[]
        q=deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node=='#':
                    st.append(node)
                    continue
                else:
                    st.append(str(node.val))
                    if node.left:
                        q.append(node.left)
                    else:
                        q.append('#')
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append('#')
        wor=",".join(st)
        print(wor)
        return wor
            

    def deserialize(self, data):
        if len(data)==0:
            return None
        i=1
        data = data.split(',')
        root=TreeNode(data[0])
        q=deque([root])
        while q and i<len(data):
            node=q.popleft()
            if i<len(data) and data[i]!='#':
                node.left=TreeNode(int(data[i]))
                q.append(node.left)
            i+=1
            if i<len(data) and data[i]!='#':
                node.right=TreeNode(int(data[i]))
                q.append(node.right)
            i+=1
        return root
        




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))