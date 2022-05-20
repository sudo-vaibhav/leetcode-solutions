#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        pre = 0
        earliest = {0:-1}
        longest = 0
        for idx,num in enumerate(arr):
            pre+=num
            if pre in earliest:
                longest = max(longest,idx-earliest[pre])
            else:
                earliest[pre]=idx
        return longest
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends