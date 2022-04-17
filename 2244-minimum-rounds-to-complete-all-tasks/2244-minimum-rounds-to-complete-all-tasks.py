class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ct = Counter(tasks)
        n = len(tasks)
        steps = 0
        
        for level in ct:
            if ct[level]<2:
                return -1
            if ct[level]%3==0:
                steps+= ct[level]//3
            else:
                steps+= 1+(ct[level]//3)
        return steps
        
        