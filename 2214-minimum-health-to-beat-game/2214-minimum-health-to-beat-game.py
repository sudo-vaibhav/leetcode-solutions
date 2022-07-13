class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        n = len(damage)
        
#         returns min health needed

        @cache
        def solve(fightIdx,canUseArmor):
            if fightIdx<0:
                return 0
            if fightIdx == n-1:
                ex = 1
            else:
                ex = 0
            dam = damage[fightIdx]
            ans = inf
            if canUseArmor:
                ans = min(ans,ex+max(0,dam-armor)+solve(fightIdx-1,False))
            ans = min(ans,ex+dam+solve(fightIdx-1,canUseArmor))
            
            return ans
        
        return solve(n-1,True)