class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        
        for level in range(1,n+1):
            vals = [1]*level
            for element in range(1,level+1):
                if element==1 or element==level:
                    pass
                else:
                    vals[element-1] = ans[-1][element-2]+ans[-1][element-1]
            ans.append(vals)
        return ans