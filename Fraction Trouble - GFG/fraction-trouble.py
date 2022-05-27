#User function Template for python3
import math as mt
class Solution:
	def numAndDen(self, n, d):
        # ans,N,D,V = 0,-1,-1,n/d
        # for i in range(1,10001):
        #     l,r = floor(ans*i),i
        #     while l<=r:
        #         j = l+(r-l)//2
        #         val = j/i
        #         if val<V:
        #             if val>ans:
        #                 ans = val
        #                 N,D = j,i
        #             l = j+1
        #         else:
        #             r = j-1
        # return [N,D]
        num=-1
		den=1
	    f=d+1
		for i in range (f,10001):
		    x=(n*i)//d
		    if mt.gcd(x,i)==1:
		        if (1.0*x/i>1.0*num/den):
		            num=x
		            den=i
	    return (num,den)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,d = input().split()
		n=int(n)
		d=int(d)
		ob = Solution();
		ans = ob.numAndDen(n,d)
		for i in range(len(ans)):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends