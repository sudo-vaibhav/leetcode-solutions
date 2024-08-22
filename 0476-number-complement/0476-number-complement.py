class Solution:
    def findComplement(self, num: int) -> int:
        # 101
        # 100
        # 010
        # return ~num
        ans = []
        while num!=0:
            ans.append(0 if num&1==1 else 1)
            num>>=1
        # print()
        return int("".join(map(str,ans[::-1])),2)