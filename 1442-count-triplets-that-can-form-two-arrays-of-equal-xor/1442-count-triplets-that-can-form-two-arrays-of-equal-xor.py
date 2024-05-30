class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        r = 0
        n = len(arr)
        ans = 0
        for k in range(n):
            r ^= arr[k]
            t = 0
            seen = defaultdict(list)
            seen[0]=[0]
            for j in range(k):
                t ^= arr[j]
                rhs = r ^ t
                lhs_target = t^rhs
                # print(r,rhs,lhs_target,seen)
                # if  in seen:
                ans += len(seen[lhs_target])
                # print(len(seen[lhs_target]),seen[lhs_target],j,k)
                seen[t].append(j)
        return ans