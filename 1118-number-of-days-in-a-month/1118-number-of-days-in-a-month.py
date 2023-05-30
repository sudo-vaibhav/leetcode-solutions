class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
    
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month==2 and ((year%100==0 and year%400==0) or (year%100!=0 and year%4==0)):
            return 29
        elif month==2:
            return 28
        return 30