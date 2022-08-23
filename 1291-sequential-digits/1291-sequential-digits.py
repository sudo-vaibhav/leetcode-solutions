class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        seq = "123456789"
        n = len(seq)
        nums = []
        for start in range(n):
            for end in range(start,n):
                cur = int(seq[start:end+1])
                if low<=cur<=high:
                    nums.append(cur)
        return sorted(nums)