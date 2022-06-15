# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         ans = []
#         def vlr(root):
#             if not root: return
#             ans.append(root.val)
#             vlr(root.left)
#             vlr(root.right)
        
#         vlr(root)
#         return ans

#         vlr
#         temp = root
#         ans = []
#         while temp:
#             if not temp.left:
#                 ans.append(temp.val)
#                 temp = temp.right
#             else:
#                 rightmostLeaf = temp.left
#                 while rightmostLeaf.right and rightmostLeaf.right!=temp:
#                     rightmostLeaf = rightmostLeaf.right
                
#                 if rightmostLeaf.right==None:
#                     ans.append(temp.val)
#                     rightmostLeaf.right = temp
#                     temp = temp.left
#                 else:
#                     rightmostLeaf.right = None
#                     temp = temp.right
#         return ans

        preorder = []
        postorder = []
        inorder = []
        
        if not root:return []
        st = deque()
        st.append((root,1))
        while st:
            cur,v = st.pop()
            val = cur.val
            if v==1:
                preorder.append(val)
                v+=1
                st.append((cur,v))
                if cur.left:
                    st.append((cur.left,1))
            elif v==2:
                inorder.append(val)
                v+=1
                st.append((cur,v))
                if cur.right:
                    st.append((cur.right,1))
            else:
                postorder.append(val)
        
        
        
#         print(preorder)
#         print(inorder)
#         print(postorder)
        
        
        return preorder
        
        
        
        
        
        
        
        
        
        
        
        