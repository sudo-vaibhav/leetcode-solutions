class Solution:
    def minPartitions(self, n: str) -> int:
        v = max(map(int,list(n)))
        return v