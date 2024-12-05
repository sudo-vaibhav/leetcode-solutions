class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if Counter(start)!=Counter(target):
            return False
        j = 0
        s = list(filter(lambda x:x!="_",start))
        t = list(filter(lambda x:x!="_",target))    
        if s!=t:
            return False
        if "R" in start:
            if start.index("R")>target.index("R"):
                # print("rviolated")
                return False
            if start.rindex("R")>target.rindex("R"):
                # print("rviolated")
                return False
        if "L" in start:
            if start.rindex("L")<target.rindex("L"):
                # print("lviolated")
                return False
            if start.index("L")<target.index("L"):
                return False
        
        return True