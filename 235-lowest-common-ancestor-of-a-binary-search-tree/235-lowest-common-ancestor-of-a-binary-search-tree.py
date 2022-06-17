class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root
        smaller = p if p.val<q.val else q
        larger = p if smaller==q else q
        while temp:
            if temp==smaller or temp==larger or smaller.val<temp.val<larger.val:
                return temp
            if larger.val<temp.val:
                temp = temp.left
            else:
                temp = temp.right
        return temp
            