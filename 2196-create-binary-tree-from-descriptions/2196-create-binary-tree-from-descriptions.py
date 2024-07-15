# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodemap = defaultdict(dict)
        parents = set()
        nodes = set()
        for p,c,isLeft in descriptions:
            # nodemap[p].val = p
            nodemap[p][isLeft] = c
            parents.add(p)
            # nodes.add(p)
            nodes.add(c)
        root = list(parents.difference(nodes))[0]
        
        
        def populate(val):
            # if val==None:
            #     return None
            temp = nodemap[val]
            return TreeNode(val,populate(temp[True]) if True in temp else None ,populate(temp[False])  if False in temp else None  )
        return populate(root)
            
        