class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        minSeen = {}
        ans =-1
        for idx, c in enumerate(s):
            
            if c not in minSeen:
                minSeen[c]=idx
            else:
                ans = max(ans,idx-minSeen[c]-1)
                # minSeen[c]=idx
        return ans