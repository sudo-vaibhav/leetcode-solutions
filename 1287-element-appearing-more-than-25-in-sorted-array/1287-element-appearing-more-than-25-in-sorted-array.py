class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c  = Counter(arr)
        
        for k in c:
            if c[k]>len(arr)/4:
                return k