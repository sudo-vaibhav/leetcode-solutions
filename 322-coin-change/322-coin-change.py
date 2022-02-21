class Solution:
    @cache
    def solve(self,n,amount):
        if amount == 0 : return 0
        if amount<0 : return -1
        if(n==0): return -1 
        
        coinVal = self.coins[n-1] # 5
        
        res1 = self.solve(n,amount-coinVal) # amount = -2
        res2 = self.solve(n-1,amount) # n = 2
        
        if(res1==-1):
            return res2
        
        if(res2 == -1):
            return 1+res1
        return min(1+res1,res2)
        
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins # [1,2,5]
        n = len(coins) # 3
        return self.solve(n,amount)