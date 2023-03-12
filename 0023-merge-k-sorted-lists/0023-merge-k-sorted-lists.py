# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        c = 0
        hp = []
        for _,l in enumerate(lists):
            if l:
                heappush(hp,(l.val,c,l))
            c+=1
        temp = ListNode()
        dummy = temp
        while hp:
            cur = heappop(hp)

            temp.next = cur[2]
            
            temp = temp.next
            
            if cur[2].next:
                heappush(hp,(cur[2].next.val,c,cur[2].next))
                c+=1
            temp.next = None 
        
        return dummy.next
        