class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
#         prev = None
        
#         def vlr(node):
#             nonlocal prev
#             if not node: return
#             L,R = node.left,node.right
#             if prev:
#                 prev.right = node
#             prev = node
#             node.left = None
#             vlr(L)
#             vlr(R)
#         vlr(root)

        # prev= None
        temp = root
        
        while temp:
            if temp.left:
                rightMost = temp.left
                while rightMost.right:
                    rightMost = rightMost.right
                
                rightMost.right = temp.right
                temp.right = temp.left
                temp.left = None
            temp = temp.right
        