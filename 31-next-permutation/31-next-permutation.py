class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        n = len(a)
        for i in range(n-2,-1,-1):
            if a[i]<a[i+1]:
                break
        else:
            a.sort()
            return
        # now i has the index where increasing part of permutation ends
        # print(a[i])
        for j in range(n-1,i,-1):
            if a[j]>a[i]:
                a[j],a[i] = a[i],a[j]
                break
        # print(a)
        a[i+1:] = a[i+1:][::-1]
        
        
        