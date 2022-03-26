class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap,-num)
        s = sum(nums)
        # print(s)
        S = s
        c=0
        while s>S/2:
            c+=1
            biggest = -heappop(heap)
            # print(biggest)
            s-=biggest
            biggest/=2
            s+=biggest
            heappush(heap,-biggest)   
        return c