class Solution:
    def checkIfPangram(self, sent: str) -> bool:
        ctr = defaultdict(int)
        for i in sent: ctr[i]+=1
        return len(ctr)==26