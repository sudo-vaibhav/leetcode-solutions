# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        
        q = deque([[root,None,""]])
        
        while q:
            lenQ = len(q)
            # print(q)
            seen = set()
            for _ in range(lenQ):
                
                node,parent,place = q.pop()
                if node.right:
                    if node.right.val in seen:
                        # print("found",node.val)
                        if place=="left":
                            parent.left = None
                        else:
                            parent.right = None
                        # parent = None
                        # node=None
                        return root
                    q.appendleft((node.right,node,"right"))
                    # seen.add(node.right.val)

                if node.left:
                    q.appendleft((node.left,node,"left"))
                seen.add(node.val)
                
                