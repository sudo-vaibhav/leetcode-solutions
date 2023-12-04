class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        ansVal = ""
        for i in range(len(num)-2):
            cur = num[i:i+3]
            if len(Counter(cur))==1:
                if int(cur)>ans:
                    ans = int(cur)
                    ansVal = cur
        
        return ansVal