class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        n = len(a)
        for i in range(n-2,-1,-1):
            if a[i]<a[i+1]:
                for j in range(n-1,i,-1):
                    if a[j]>a[i]:
                        a[j],a[i] = a[i],a[j]
                        break
                a[i+1:] = a[i+1:][::-1]
                return
        a.sort()
        
        
        
        