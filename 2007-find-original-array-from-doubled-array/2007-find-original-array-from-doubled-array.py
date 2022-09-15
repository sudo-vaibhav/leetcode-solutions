from sortedcontainers import SortedList

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        l = SortedList(changed)
        ans = []
        while l:
            smallest = l[0]
            l.discard(smallest)
            if 2*smallest not in l:
                return []
            ans.append(smallest)
            l.discard(2*smallest)
        return ans