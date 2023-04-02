class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        for s in spells:
            target = success/s
            index = bisect_left(potions,target)
            ans.append(len(potions)-index)
        
        return ans