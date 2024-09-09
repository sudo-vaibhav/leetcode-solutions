# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = [[-1]*n for _ in range(m)]
        
        d = "R"
        seen = set([(0,0)])
        afterMap = {
            "R" : "D",
            "D" : "L",
            "L" : "U",
            "U" : "R"
        }
        moveMap = {
            "R" : (0,1),
            "U" : (-1,0),
            "L" : (0,-1),
            "D" : (1,0)
        }
        
        temp = head
        i,j = 0,0
        while temp:
            di,dj = moveMap[d]
            arr[i][j] = temp.val
            I,J = i+di,j+dj
            if not (0<=I<m and 0<=J<n and (I,J) not in seen):
                d = afterMap[d]
                di,dj = moveMap[d]
                I,J = i+di,j+dj
            # else:
            #     seen.add((I,J))
            seen.add((I,J))
            i,j = I,J
            temp = temp.next
        return arr