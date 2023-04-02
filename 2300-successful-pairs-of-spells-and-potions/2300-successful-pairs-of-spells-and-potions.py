class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        return potions.sort() or [len(potions)-bisect_left(potions,success/s) for s in spells]
        