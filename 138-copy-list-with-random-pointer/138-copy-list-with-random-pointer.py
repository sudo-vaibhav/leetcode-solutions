class Solution:    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        temp = head
        while temp:
            temp.next = Node(temp.val,temp.next)
            temp = temp.next.next
        temp = head
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        newHead = head.next
        temp = head
        while temp:
            nextOldNode = temp.next.next
            curNewNode = temp.next
            curNewNode.next = nextOldNode.next if nextOldNode else None
            temp.next = nextOldNode
            temp = nextOldNode
        return newHead