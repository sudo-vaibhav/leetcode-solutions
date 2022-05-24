class Solution:
    def maximum69Number (self, num: int) -> int:
        N = list(str(num))
        try:
            six = N.index("6")
            N[six]="9"
            return int("".join(N))
        except:
            return num