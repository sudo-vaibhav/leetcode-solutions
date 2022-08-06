class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets)/log(minutesToTest/minutesToDie+1))
        if buckets==1:
            return 0
        
        
        l,r = 1,buckets
        ans = r
        def isPos(pigCount):
            pc = pigCount
            perBucket = ceil(buckets/pigCount)
            time = minutesToDie
            pos = True
            while perBucket>1:
                if pigCount==1:
                    pos = False
                    break
                time += minutesToDie
                pigCount-=1
                perBucket = ceil(perBucket/pigCount)
            print(pos,pc,time,minutesToTest)
            return time<=minutesToTest
             
        while l<=r:
            m = l+(r-l)//2
            print(m)
            if isPos(m):
                ans = min(ans,m)
                r = m-1
            else:
                l = m+1
        
        return ans