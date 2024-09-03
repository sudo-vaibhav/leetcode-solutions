class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = "".join(map(str,[ord(c)-ord("a")+1 for c in s]))
        while k:
            temp = str(sum(map(int,temp)))
            k-=1
        return int(temp)