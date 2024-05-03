class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
        def solve(v1,v2):
            if len(v1)>len(v2):
                return -solve(v2,v1)
            while len(v1)<len(v2):
                v1.append(0)
            # print(v1,v2)
            i = 0
            while i<len(v1):
                cur1 = v1[i]
                cur2 = v2[i]
                if cur1<cur2:
                    return -1
                elif cur1>cur2:
                    return 1
                i+=1
            return 0
        
        return solve(list(map(int,v1.split("."))),list(map(int,v2.split("."))))
        