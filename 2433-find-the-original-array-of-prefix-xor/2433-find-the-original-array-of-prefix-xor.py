class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        temp = 0
        
        ans = []
        
        for num in pref:
            ans.append(temp^num)
            temp^=ans[-1]
        return ans