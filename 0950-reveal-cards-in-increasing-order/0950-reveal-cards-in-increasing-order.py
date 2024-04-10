class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [0]*n
        
        s = list(sorted(deck))
        
        ind = deque(range(n))
        
        for c in s:
            ans[ind.popleft()]=c
            if ind:
                ind.append(ind.popleft())
        return ans