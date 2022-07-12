class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        nextOcc = [n]*n
        prevOcc = [-1]*n
        occ = defaultdict(lambda:n)
        for i in range(n-1,-1,-1):
            nextOcc[i] = occ[s[i]]
            occ[s[i]]=i
        occ = defaultdict(lambda:-1)
        for i in range(n):
            prevOcc[i] = occ[s[i]]
            occ[s[i]]=i
        ans = 0
        for i in range(n):
            ans += (nextOcc[i]-i)*(i-prevOcc[i])
        return ans