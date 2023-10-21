class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        
        def sumOfAP(l,r):
            endVal = books[i]
            
            cnt = min(r-l+1,books[i])
            firstVal = endVal-(cnt-1)
            return (cnt*(firstVal+endVal))//2
        
        st = []
        dp = [0]*n
        ans = 0
        for i in range(len(books)):
            
            while st and books[st[-1]]>books[i]-(i-st[-1]):
                st.pop()
                
            if st:
                dp[i] = dp[st[-1]]+sumOfAP(st[-1]+1,i)
            else:
                dp[i] = sumOfAP(0,i)
            
            st.append(i)
        return max(dp)
            