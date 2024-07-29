from sortedcontainers import SortedSet
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.solve(rating)+self.solve(rating[::-1])
    
    def solve(self,arr):
        s2 = SortedSet(arr)
        s1 = SortedSet()
        ans = 0
        for i in range(0,len(arr)):
            ans += s1.bisect_right(arr[i]-1)*(len(s2)-s2.bisect_left(arr[i]+1))
            s1.add(arr[i])
            s2.remove(arr[i])
        return ans
            
        
