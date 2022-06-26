class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        isBST, minVal, maxVal, sum = range(4)
        def solve(node):
            nonlocal ans
            if not node: return (True,inf,-inf,0)
            L,R = solve(node.left),solve(node.right)
            if L[isBST] and R[isBST] and L[maxVal]<node.val<R[minVal]:
                tempSum = L[sum]+R[sum]+node.val
                ans = max(ans,tempSum)
                return (True,min(node.val,L[minVal],R[minVal]),max(node.val,L[maxVal],R[maxVal]),tempSum)
            return tuple([False,"""rest params dont matter anyways now"""])
        solve(root)
        return ans