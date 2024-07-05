# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        temp = head
        points = []
        i = 0
        while temp.next:
            if prev:
                if prev.val>temp.val<temp.next.val:
                    # local minima
                    points.append(i)
                    
                elif prev.val<temp.val>temp.next.val:
                    # local maxima
                    points.append(i)
            prev = temp
            temp = temp.next
            i+=1
        
        if len(points)<2:
            return [-1,-1]
        # print("hey")
        # for p in points:
        #     print(p.val)
        c = 0
        # print(points)
        a1,a2 = inf,-inf
        for i in range(1,len(points)):
            a1 = min(a1,points[i]-points[i-1])
            # a2 = max(a2,points[i]-points[i-1])
        return [a1,points[-1]-points[0]]