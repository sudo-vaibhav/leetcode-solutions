#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
        n = len(s)
        ans = []
        def solve(i,path):
            if i==n:
                if path:
                    ans.append("".join(path))
            else:
                solve(i+1,path)
                path.append(s[i])
                solve(i+1,path)
                path.pop()
        solve(0,[])
        return sorted(ans)
                    
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends