class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total,cur = 0,0
        idx = 0
        for i in range(len(gas)):
            if cur<0:
                idx = i
                cur = 0
            
            total += gas[i]
            total -= cost[i]
            
            cur += gas[i]
            cur -= cost[i]
        if total<0:
            return -1
        return idx