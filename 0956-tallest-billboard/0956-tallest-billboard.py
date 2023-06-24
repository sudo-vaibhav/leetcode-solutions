class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        n = len(rods)
        left_half = rods[:n//2]
        right_half = rods[n//2:]
        def helper(arr):
            seen_combos = set([(0,0)])
            for r in arr:
                new_states = set()
                for left, right in seen_combos:
                    new_states.add((left + r, right))
                    new_states.add((left, right + r))
                seen_combos |= new_states
            dp = {}
            for left,right in seen_combos:
                dp[left-right] = max(dp.get(left-right,0),left)
            return dp
            
        # diff = left - right
        diff_to_left_height_map_1 = helper(left_half)
        diff_to_left_height_map_2 = helper(right_half)
        
        
        ans = 0
        for diff in diff_to_left_height_map_1:
            left_height_1 = diff_to_left_height_map_1[diff]
            
            if -diff in diff_to_left_height_map_2:
                left_height_2 = diff_to_left_height_map_2[-diff]
                ans = max(left_height_1+left_height_2,ans)
        return ans