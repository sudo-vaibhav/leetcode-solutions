class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        ans = "0"
        for i in range(0,n,1):
            
            if number[i]==digit:
                # print(i)
                temp =  number[:i]+number[i+1:]
                # print(temp)
                if temp=="": temp="0"
                if int(temp)>int(ans):
                    ans = temp
        return ans