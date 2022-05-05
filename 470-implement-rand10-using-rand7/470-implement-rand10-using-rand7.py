# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        ans = 11
        while ans>10 or ans<1:
            row,col = rand7(),rand7()
            idx = ((row-1)*7)+col
            
            if idx>40:
                continue
            else:
                ans = idx%10
                if ans==0:
                    ans = 10
                
            
        
        return ans
        