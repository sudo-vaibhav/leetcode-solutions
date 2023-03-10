# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.list = []
        
        temp = head
        while temp:
            self.list.append(temp)
            temp = temp.next
        
        

    def getRandom(self) -> int:
        return random.choice(self.list).val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()