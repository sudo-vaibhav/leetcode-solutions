# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        i = 0
        temp = head
        m = {}
        # n=0
        while temp:
            m[i]=temp
            temp = temp.next
            i+=1
        n=i
        dummy = ListNode()
        temp = dummy
        for i in range(n):
            cur = m[i//2] if i%2==0 else m[n-ceil(i/2)]
            # print(cur.val)
            temp.next = cur
            temp = cur
        # print()
        temp.next = None
        return dummy.next
            
                
                