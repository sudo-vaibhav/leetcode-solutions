class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ct = Counter(arr)
        v = ct.values()
        return len(set(v))==len(v)