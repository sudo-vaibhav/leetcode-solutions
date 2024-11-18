class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k==0:
            return [0]*n
        elif k<0:
            return self.decrypt(code[::-1],-k)[::-1]
        else:
            ans = [0]*n
            for i in range(n):
                j = (i+1)%n
                tempK = k
                temp = 0
                while tempK>0:
                    temp += code[j]
                    j = (j+1)%n
                    tempK-=1
                ans[i]=temp
            return ans