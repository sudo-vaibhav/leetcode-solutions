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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        
        def count(head):
            c=0
            temp = head
            while temp:
                c+=1
                temp = temp.next
            return c
        
        n = count(head)
        
        def solve(l,r):
            nonlocal head
            if l>r: return None
            mid = (l+r)//2
            left = solve(l,mid-1)
            t = TreeNode(head.val)
            t.left = left
            head = head.next
            t.right = solve(mid+1,r)
            return t
        
        return solve(0,n-1)