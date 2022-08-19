class Solution:
    def isPossible(self, nums: List[int]) -> bool:
    # my algorithm
    
    # 1. iterate over element of array and for each element
    # 2. check its previous number => check if we have a subsequence ending at prev (if multiple are present
    #     pick that one which is of shorter length (use pq for this))
    # 3. if subsequence ending at prev is not present, add a new subsequence ending at cur of length 1
    # 4. if subsequence ending at prev is present, remove subsequence ending at prev, and create a new one ending at cur with one more length are length of prev subsequence.
    # 5. in the end check if all current present subsequences have length more than or equal to 3.


    #DRY RUN
    #         [1,2,3,3,4,4,5,5]
    # 1=> {1:[1,]} // all the arrays are minheaps
    # 2=> {2:[2]}
    # 3=> {3:[3]}
    # 4=> {3:[1,3]}
    # 5=> {3:[3],4:[2]}
    # 6=> {4:[2,4]}
    # 7=> {4:[4],5:[3]}
    # 8=> {5:[3,5]}

    # O(nlogn) time and O(n) space soln
#         d = defaultdict(list)
#         for num in nums:
#             prev = num-1

#             if d[prev]:
#                 prevLen = heappop(d[prev])
#                 heappush(d[num],prevLen+1)
#             else:
#                 heappush(d[num],1)
#         for k in d:
#             for v in d[k]:
#                 if v<3:
#                     return False
#         return True

#     O(n) time and O(n) space soln
        subseq = defaultdict(int)
        freq = Counter(nums)
        for num in nums:
            if freq[num]==0:continue
            if subseq[num-1]>0:
                subseq[num-1]-=1
                subseq[num]+=1
            elif freq[num+1] and freq[num+2]:
                subseq[num+2]+=1
                freq[num+1]-=1
                freq[num+2]-=1
            else:
                return False
            freq[num]-=1
        
        return True