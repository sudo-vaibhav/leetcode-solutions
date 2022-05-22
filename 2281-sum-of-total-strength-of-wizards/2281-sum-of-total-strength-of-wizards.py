class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        nextSmaller = [n]*n
        MOD = 7 + 10**9
        stack = deque()
        
        for i in range(n-1,-1,-1):
            cur = strength[i]
            while len(stack)>0 and strength[stack[-1]]>=cur:
                stack.pop()
            if len(stack)>0:
                nextSmaller[i] = stack[-1]
            stack.append(i)
            
        stack = deque()
        
        prevSmaller = [-1]*n
        
        for i in range(n):
            cur = strength[i]
            while len(stack)>0 and strength[stack[-1]]>cur:
                stack.pop()
            if len(stack)>0:
                prevSmaller[i] = stack[-1]
            stack.append(i)
        
        # print(nextSmaller,prevSmaller)
        
        prefixSum = [0]
        for num in strength:
            prefixSum.append((prefixSum[-1]+num)%MOD)
        
        ppSum = [prefixSum[0]]
        for i in range(1,len(prefixSum)):
            ppSum.append((prefixSum[i]+ppSum[-1])%MOD)
        
        # print(prefixSum,ppSum)
        
#         for given index i , where i is the index with smallest value, and its prev Smaller and next Smaller are prev and n
#         the elements would appear as such
#         prev+1 to i, prev+1 to i+1, prev+1 to i+2, ... prev+1 to n-1
#         prev+2 to i, prev+2 to i+1, prev+2 to i+2, ... prev+2 to n-1
# ...
#         i to i,      i to i+1,      i to i+2, ...      i to n-1
        
#      translating the above to prefix Sum analogies

#         pref[i+1]-pref[prev], pref[i+2]-pref[prev], pref[i+3]-pref[prev],... pref[n]-pref[prev]
#         pref[i+1]-pref[prev+1], pref[i+2]-pref[prev+1], pref[i+3]-pref[prev+1],...pref[n]-pref[prev+1]
#         pref[i+1]-pref[prev+2], pref[i+2]-pref[prev+2], pref[i+3]-pref[prev+2],...pref[n]-pref[prev+2]
# ...
#         pref[i+1]-pref[i], pref[i+2]-pref[i], ...      pref[n]-pref[i]


# now we need to efficiently find the accumulated sum of all the entries listed above for each index in constant time per index. For that we need to compress the above terms

#        pref[i+1],pref[i+2],pref[i+3]... pref[n] are used with positive sign row number of times, which is i-prev+1 times
#        pref[prev],pref[prev+1],pref[prev+2],... pref[i] are each used with negative sign col number of times, which is n-i times 

# or basically its overall, (prefpref[n+1]-prefpref[i])*(i-prev+1)
# plus (prefpref[i+1]-prefpref[prev+1])*(n-i)
        
        ans = 0
        for i in range(n):
            prev = prevSmaller[i]
            nex = nextSmaller[i]
            
            minus = ((ppSum[i]-(0 if prev==-1 else ppSum[prev]))*(nex-i))%MOD
            plus = ((ppSum[nex]-ppSum[i])*(i-prev))%MOD
            
            # print(i,prev,nex,plus,minus)
            ans += (strength[i]*(plus-minus))%MOD

        return ans%MOD