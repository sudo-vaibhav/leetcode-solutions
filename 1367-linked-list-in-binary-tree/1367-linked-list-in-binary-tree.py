# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            @cache
            def solve(node,curHead):
                if not curHead:
                    return True
                if not node:
                    return False
                ans = False
                if curHead.val == node.val:
                    ans = solve(node.left,curHead.next) or solve(node.right,curHead.next)
                if not ans:
                    ans = solve(node.left,head) or solve(node.right,head)
                return ans
            return solve(root,head)