class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        start,end,bank = list(start),list(end),list(map(list,bank)) 
        visited = set()
        chars = ["A","C","G","T"]
        def solve(cur):
            if cur==end: return 0
            minsteps = inf
            
            for i in range(8):
                temp = list(cur)
                for mut in chars:
                    temp[i]=mut
                    if temp in bank and "".join(temp)!="".join(cur) and tuple(temp) not in visited:
                        visited.add(tuple(temp))
                        minsteps = min(minsteps,1+solve(temp))
            
            return minsteps
        x=solve(start)
        return x if x!=inf else -1 