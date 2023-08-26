class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        
        
        ans = 1
        prev = pairs[0]
        for s,e in pairs[1:]:
            if s>prev[1]:
                ans+=1
                prev=s,e
        # print(pairs)
        return ans