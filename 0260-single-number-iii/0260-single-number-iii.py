class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for i in nums:
            x^=i
        
        set_bit_pos = 0
        
        while not x&1<<set_bit_pos:
            set_bit_pos += 1
        
        ans = [0,0]
        for i in nums:
            if i&1<<set_bit_pos:
                ans[0]^=i
            else:
                ans[1]^=i
        return ans
        
        