class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        for place in range(n):
            temp = 0
            for pickFrom in range(n):
                temp += abs(pickFrom-place) if boxes[pickFrom]=="1" else 0
            ans.append(temp)
        
        return ans