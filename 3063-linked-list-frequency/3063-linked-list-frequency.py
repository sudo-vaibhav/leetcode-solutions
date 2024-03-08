# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            dummy = ListNode()
            
            temp = head
            c = defaultdict(int)
            
            while temp:
                c[temp.val]+=1
                temp = temp.next
            temp = dummy
            for v in c.values():
                temp.next = ListNode(v)
                temp = temp.next
            
            return dummy.next