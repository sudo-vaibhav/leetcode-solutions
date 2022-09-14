# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        def onlyOneOddNum(counter):
            ans = 0
            for k in counter:
                ans += counter[k]%2==1
            return ans<=1
        def traverse(root,ctr=defaultdict(int)):
            nonlocal res
            ctr[root.val]+=1
            if not root.left and not root.right:
                # print(ctr)
                res+=onlyOneOddNum(ctr)
            else:
                if root.left: traverse(root.left,ctr)
                if root.right: traverse(root.right,ctr)
            ctr[root.val]-=1
        traverse(root)
        return res
            