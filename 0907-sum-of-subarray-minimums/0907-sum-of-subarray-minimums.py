class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        st = []
        MOD = 10**9+7
        prevSmaller = [-1]*n
        for i in range(n):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                prevSmaller[i]=st[-1]
            st.append(i)
        # print(prevSmaller,st)
        st = []
        nexSmaller = [n]*n
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                nexSmaller[i]=st[-1]
            st.append(i)
        ans = 0
        for i in range(n):
            p,q = prevSmaller[i],nexSmaller[i]
            P,Q = i-p,q-i
            ans += P*Q*arr[i]
            if ans>=MOD:ans-=MOD
        
        return ans