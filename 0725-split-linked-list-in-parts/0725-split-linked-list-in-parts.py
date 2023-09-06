# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        size = 0
        
        temp = head
        while temp:
            size+=1
            temp = temp.next
        
        per_list = ceil(size/k)
        ans = []
        running = head
        while k>0:
            dummy = ListNode()
            temp = dummy
            take = 1
            if (k-1)*(per_list-1)<=size-per_list:
                take = max(per_list,take)
            else:
                take = max(per_list-1,take)
            while take>0 and running:
                temp.next = running
                temp = temp.next
                running = running.next
                take-=1
                size-=1
            temp.next = None
            
            ans.append(dummy.next)
            k-=1
        
        return ans