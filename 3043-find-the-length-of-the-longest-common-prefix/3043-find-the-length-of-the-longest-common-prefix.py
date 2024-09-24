class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1,arr2 = map(lambda x:map(str,x),[arr1,arr2])
        pres = set()
        for w in arr1:
            running = ""
            for c in w:
                running += c
                pres.add(running)
        ans = 0
        for w in arr2:
            running = ""
            for c in w:
                running += c
                if running in pres:
                    ans = max(ans,len(running))
        return ans