class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        continuousCounts = []
        prev = "-"
        for i in s:
            if i!=prev:
                continuousCounts.append(1)
                prev = i
            else:
                continuousCounts[-1]+=1
        s=0
        for i in range(1,len(continuousCounts)):
            s+=min(continuousCounts[i],continuousCounts[i-1])
            
        return s
                