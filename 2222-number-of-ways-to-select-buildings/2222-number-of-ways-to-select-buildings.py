class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = 0
        oneCountTill = defaultdict(int)
        zeroCountTill = defaultdict(int)
        
        for idx,building in enumerate(s):
            oneCountTill[idx] = oneCountTill[idx-1]+(1 if building=='1' else 0)
            zeroCountTill[idx] = zeroCountTill[idx-1]+(1 if building == '0' else 0)
        n = len(s)
        # print(n)
        # print(oneCountTill)
        # print(zeroCountTill)
        for idx,building in enumerate(s):
            if building == '0':
#                 office
                a,b= oneCountTill[idx-1],(oneCountTill[n-1]-oneCountTill[idx])
            else:
#         restaurant
                a,b= zeroCountTill[idx-1],(zeroCountTill[n-1]-zeroCountTill[idx])
            # print(idx,a,b)
            ans+=a*b
    
        return ans
        