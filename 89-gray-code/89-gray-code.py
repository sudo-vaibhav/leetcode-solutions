class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        used = set([0])
        ans = [0]
        
        while len(ans)!=2**n:
            prev = ans[-1]
            i = 0
            while (1<<i)<2**n:
                temp = prev^(1<<i) 
                if temp not in used:
                    ans.append(temp)
                    used.add(temp)
                    break
                i+=1
        return ans
        