class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        TR = lambda : defaultdict(TR)
        tr = TR()
        ENDS = "ends"
        ans = []
        folder.sort() #so that parents come before children
        for f in folder:
            ps = f.split("/")
            temp = tr
            isChild=False
            for p in ps:
                temp = temp[p]
                if temp[ENDS]==True:
                    isChild=True
                    break
            if not isChild:
                ans.append(f)
                temp[ENDS]=True
        return ans
        
        