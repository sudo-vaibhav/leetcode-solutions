class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        @cache
        def highestInRight(i):
            if i>n-1:
                return 0
            if i==n-1:
                return height[i]
            else:
                return max(height[i],highestInRight(i+1))
        @cache
        def highestInLeft(i):
            if i==0:
                return height[i]
            else:
                return max(height[i],highestInLeft(i-1))
        
        for i in range(n):
            cur = height[i]
            r = highestInRight(i)
            l = highestInLeft(i)
            ans += max(0,min(r,l)-cur)
        return ans