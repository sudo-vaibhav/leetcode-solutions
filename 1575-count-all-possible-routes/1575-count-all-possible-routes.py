class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10**9+7
        
        @cache
        def solve(idx,fuel):
            # if fuel==0:
            #     if idx==finish: return 1
            ans = int(idx==finish)
            for nextStop in range(n):
                fuelNeeded = abs(locations[idx]-locations[nextStop])
                if nextStop!=idx and fuelNeeded<=fuel:
                    ans += solve(nextStop,fuel-fuelNeeded)          
                # if idx==finish:
                #     ans += 1
                    
            return ans%MOD
        return solve(start,fuel)
        
        
        
        
        
        