# class Solution:
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         def lvr(root):
#             if not root: return []
#             return [*lvr(root.left),root,*lvr(root.right)]
        
#         trav = lvr(root)
#         sted = sorted(trav,key=lambda x:x.val)
#         viol1,viol2,n = inf,inf,len(trav)
#         for i in range(n):
#             if trav[i].val!=sted[i].val:
#                 if viol1==inf:
#                     viol1=trav[i]
#                 else:
#                     viol2=trav[i]
#                     break
#         viol1.val,viol2.val = viol2.val,viol1.val

# class Solution:
#     def __init__(self):
#         self.prev = TreeNode(float("-inf"))
#         self.first = None
#         self.second = None
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         def lvr(root):
#             if not root: return
#             lvr(root.left)
            
#             if self.prev.val > root.val and not self.first:
#                 self.first = self.prev
#             if self.prev.val > root.val and self.first:
#                 self.second = root
#             self.prev = root
#             lvr(root.right)
        
#         lvr(root)    
#         self.first.val,self.second.val = self.second.val,self.first.val

class Solution:
    def __init__(self):
        self.prev = TreeNode(float("-inf"))
        self.first = None
        self.second = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def check(root):
            if self.prev.val > cur.val and not self.first:
                self.first = self.prev
            if self.prev.val > cur.val and self.first:
                self.second = cur
            self.prev = cur
        cur = root
        while cur:
            if not cur.left:
                check(cur)
                cur = cur.right
            else:
                temp = cur.left
                while temp.right and temp.right != cur:
                    temp = temp.right
                if temp.right!=cur:
                    temp.right = cur
                    cur = cur.left
                else:
                    temp.right = None
                    check(temp)
                    cur = cur.right
        
        self.first.val,self.second.val = self.second.val,self.first.val
