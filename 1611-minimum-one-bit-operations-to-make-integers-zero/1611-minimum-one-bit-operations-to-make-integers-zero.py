class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans
        s = str(bin(n))[2:]
        print(s)
        L = len(s)
        prev = s[-1]
        chunks = []
        for i in range(L-2,-1,-1):
            cur = s[i]
            if cur=="0":
                chunks.append(prev)
                prev = cur
            else:
                prev = cur+prev
        chunks.append(prev)
        print(chunks)
        
        def solve(c):
            ctr = Counter(c)
            return ctr["1"]+ctr["0"]*2
        
        ans = 0
        for chunk in chunks:
            ans+=solve(chunk)
        return 2