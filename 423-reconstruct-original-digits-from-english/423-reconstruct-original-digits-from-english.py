class Solution:
    def originalDigits(self, s: str) -> str:
        dig = {
            0 : "zero",
            1 : "one",
            2 : "two",
            3 : "three",
            4 : "four",
            5 : "five",
            6 : "six",
            7 : "seven",
            8 : "eight",
            9 : "nine"
        }
        ctr = Counter(s)
        # one = ctr[]
        ans = [
            ctr["z"], #0 - done
            None,     #1 
            ctr["w"], #2 - done
            None,     #3 - 
            ctr["u"], #4 - done
            None,     #5 - done
            ctr["x"], #6 - done
            None,     #7 - done
            ctr["g"], #8 - done
            None,     #9 - done
        ]
        
        ans[5] = ctr["f"]-ans[4]
        ans[7] = ctr["v"] - ans[5]
        ans[1] = ctr["o"] - ans[4] - ans[0] - ans[2]
        ans[3] = ctr["h"] - ans[8]
        ans[9] = ctr["i"] - ans[5] - ans[6] - ans[8]
        fin = ""
        for i in range(10):
            fin += str(i)*ans[i]
        return fin