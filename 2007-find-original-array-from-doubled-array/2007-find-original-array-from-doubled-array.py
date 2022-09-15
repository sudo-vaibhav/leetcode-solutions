from sortedcontainers import SortedList
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        sl = sorted(changed)
        ans = []
        items = Counter(changed)
        for elem in sl:
            if items[elem]:
                items[elem]-=1
                if items[elem*2]==0: return []
                items[elem*2]-=1
                ans.append(elem)
        return ans