class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        hp = list(sticks)
        heapify(hp)
        ans = 0
        while len(hp)>1:
            tot = heappop(hp)+heappop(hp)
            heappush(hp,tot)
            ans += tot
        return ans
        