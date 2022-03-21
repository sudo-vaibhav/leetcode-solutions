class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = {}
        for idx,c in enumerate(s): ends[c] = idx
        interval = [0,0]
        ans = []
        for idx,c in enumerate(s):
            if ends[c]>interval[1]:
                interval[1] = ends[c]
            if interval[1]==idx:
                ans.append(interval[1]-interval[0]+1)
                interval = [idx+1,idx+1]
        return ans