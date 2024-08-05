class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        t = 0
        for i in range(len(arr)):
            if c[arr[i]]==1:
                t+=1
            if k==t:
                return arr[i]
        return ""