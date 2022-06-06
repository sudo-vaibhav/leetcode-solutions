#User function Template for python3
from math import inf
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n>m:
            n,m = m,n
            arr1,arr2 = arr2,arr1
        l,r = 0,n
        
        while l<=r:
            pickedFrom1 = (l+r)//2
            pickedFrom2 = k-pickedFrom1
            
            if pickedFrom2>m:
                l = pickedFrom1+1
                continue
            elif pickedFrom2<0:
                r = pickedFrom1-1
                continue
            
            l1,l2 = -inf if pickedFrom1==0 else arr1[pickedFrom1-1],-inf if pickedFrom2==0 else arr2[pickedFrom2-1]
            r1,r2 = inf if pickedFrom1==n else arr1[pickedFrom1],inf if pickedFrom2==m else arr2[pickedFrom2]
            
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            else:
                if l1>r2:
                    r = pickedFrom1-1
                else:
                    l = pickedFrom1+1
                    
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends