class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ct = Counter(cards)
        temp = max(ct.values())
        if temp<2:
            return -1
        n = len(cards)
        prev = {}
        ans = n
        for i in range(len(cards)):
            cur = cards[i]
            if cur not in prev:
                prev[cur]= i
            else:
                ans = min(ans,i-prev[cur]+1)
                prev[cur]=i
        return ans
            