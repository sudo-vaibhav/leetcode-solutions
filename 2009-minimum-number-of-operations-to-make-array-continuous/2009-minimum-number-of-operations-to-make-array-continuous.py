class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ct = Counter(nums)
        n = len(nums)
        duplicates = 0
        for num,cnt in ct.items():
            duplicates += cnt-1
        ans = n
        sortedUniques = list(sorted(ct.keys()))
        def findReq(lower,higher):
            temp = duplicates # these have to be replaced no matter what
            l = bisect_left(sortedUniques,lower-1)
            r = bisect_right(sortedUniques,higher)
            # print(lower,higher,sortedUniques,l,r)
            uniquesInCompliance = r-(l+int(sortedUniques[l]==lower-1))
            ans = temp+len(ct)-uniquesInCompliance
            # print(lower,higher,sortedUniques,l,r,ans)
            return ans
        for cand in ct:
            lowest = cand-(n-1)
            highest = cand+(n-1)
            ans = min(ans,findReq(lowest,cand),findReq(cand,highest))
        return ans
        # then we ask how many non duplicates lie outside [lowest,highest]