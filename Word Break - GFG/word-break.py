#User function Template for python3
from functools import lru_cache
def wordBreak(line, dictionary):
    set(dictionary)
    n = len(line)
    @lru_cache(maxsize=None)
    def solve(i):
        if i==n:
            return True
        else:
            for j in range(i+1,n+1):
                if line[i:j] in dictionary and solve(j):
                    return True
            return False
    return solve(0)
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends