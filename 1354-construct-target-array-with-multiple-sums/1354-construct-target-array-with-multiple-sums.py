class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-t for t in target]
        heapify(heap)
        S = sum(target)
        while heap[0]!=-1:
            cur = -heappop(heap)
            adjustedSum = S-cur
            if cur<= adjustedSum or adjustedSum<1:return False
            if adjustedSum==1:
                return True
            adjustedCur = cur%adjustedSum
#           now readjust S value
            S = adjustedSum + adjustedCur
            heappush(heap,-(adjustedCur or S))
        return True
            