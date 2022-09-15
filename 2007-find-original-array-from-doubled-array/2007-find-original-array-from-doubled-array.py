from sortedcontainers import SortedList
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        items = [0]*(2*(10**5+1))
        for num in changed: items[num]+=1
        for elem in range(0,10**5+1):
            while items[elem]>0:
                items[elem]-=1
                if items[elem*2]==0: return []
                items[elem*2]-=1
                ans.append(elem)
        return ans