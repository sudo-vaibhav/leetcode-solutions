class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
#       set of candidates
#       target
#       hint for recursion - combination, RETURN ALL
#       constraints - will be very less, especially when generate all is there

        # unlimited number of times : unbounded knapsack
        ans = []
        ctr = Counter(candidates)
        nums = list(ctr.keys())
        N = len(nums)
#       generates and returns all combinations of the subarray from idx-> which sum to target
        def solve(idx,target):
            if idx>=N:
                if target==0:
                    return [[]]
                else:
                    return []
            else:
                cur = nums[idx]
                
#                 knapsack variation, i can choose to pick or not pick
                tempans = []
                
#               not pick i can always do
                for pickAmt in range(0,ctr[cur]+1):
                    deductedAmt = pickAmt*cur
                    
                    if deductedAmt<=target:
                        combs = solve(idx+1,target-deductedAmt)
                        for seq in combs:
                            tempans.append([cur]*pickAmt+seq)
                return tempans
#                 both pick and not pick are arrays
            
        
        return solve(0,target)
    
    
        # iterative subsets
        
        # [1,2,3,4]
#         generate all subsets
#         res = {[]}
#         res = {[],[1]}
#         res = {[],[1],[3],[1,3]}

