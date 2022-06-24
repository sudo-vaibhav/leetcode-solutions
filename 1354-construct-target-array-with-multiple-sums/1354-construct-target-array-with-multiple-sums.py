class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-t for t in target]
        heapify(heap)
        S = sum(target)
        while heap[0]!=-1:
            cur = -heappop(heap)
            adjustedSum = S-cur
            # prev = S-2*cur
            # to get prev value we need to do cur - (S-cur)
            # and push the new value back in heap, but if cur itself is too big
            # the same element will come again to be subtracted, so we use module to
            # cascade operations and make function faster
            # but module doesnt give correct result when divisor is 1 or lesser (1 always 
            # can reduce anything to any desired value)
            # if S-cur<=1:
            #     return bool(S-cur)
            if cur<= adjustedSum or adjustedSum<1:return False
            adjustedCur = cur%adjustedSum
#           now readjust S value
            S = adjustedSum + adjustedCur
            heappush(heap,-(adjustedCur or S))
        return True
            