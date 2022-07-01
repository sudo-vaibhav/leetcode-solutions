class Solution:
    def maximumUnits(self, boxes: List[List[int]], truckSize: int) -> int:
        boxes.sort(key=lambda x:(-x[1]))
        i = 0
        ans = 0
        while i<len(boxes):
            canTake = min(truckSize,boxes[i][0])
            ans += boxes[i][1]*canTake
            truckSize-=canTake
            i+=1
        return ans