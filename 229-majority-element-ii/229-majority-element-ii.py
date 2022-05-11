class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = set()
        n1,n2,ct1,ct2 = -1,-1,0,0
        for i in nums:
            if i==n1: ct1+=1
            elif i==n2: ct2+=1
            elif ct1==0:
                n1 = i
                ct1 = 1
            elif ct2==0:
                n2 = i
                ct2 = 1
            else:
                ct2-=1
                ct1-=1
        def verify(num):
            if nums.count(num)>len(nums)//3:
                ans.add(num)
        verify(n1)
        verify(n2)
        return ans