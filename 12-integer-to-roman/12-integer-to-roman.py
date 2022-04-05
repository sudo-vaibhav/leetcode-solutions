class Solution:
    def intToRoman(self, num: int) -> str:
        h = [
            (1000,"M"),
            (900,"CM"),
            (500,"D"),
            (400,"CD"),
            (100,"C"),
            (90,"XC"),
            (50,"L"),
            (40,"XL"),
            (10,"X"),
            (9,"IX"),
            (5,"V"),
            (4,"IV"),
            (1,"I"),
        ]
        
        ans = ""
        while num>0:
            for pos in h:
                if num>=pos[0]:
                    num-=pos[0]
                    ans+=pos[1]
                    break
        return ans