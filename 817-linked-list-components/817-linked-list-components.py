# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        
        class Uf():
            def make_set(self,nums):
                self.parent = defaultdict(lambda : -1)
                # {num:num for num in nums}
                self.rank = defaultdict(int)
            def union(self,n1,n2):
                p1,p2 = self.find(n1),self.find(n2)
                r1,r2 = self.rank[p1],self.rank[p2]
                if r1<r2:
                    self.parent[p1]=p2
                elif r2>r1:
                    self.parent[p2]=p1
                else:
                    if p1<p2:
                        p1,p2 = p2,p1
                    
#                     rule : greater will become parent
                    self.parent[p2] = p1
                    self.rank[p1]+=1
            def find(self,n):
                if self.parent[n]==-1:
                    return n
                else:
                    self.parent[n] = self.find(self.parent[n])
                    return self.parent[n]
        
        uf = Uf()
        uf.make_set(nums)
        temp = head
        while temp.next:
            u,v = temp.val,temp.next.val
            if u in nums and v in nums:
                uf.union(u,v)
            temp = temp.next
        
        t = []
        for num in nums:
            t.append(uf.find(num))
        return len(Counter(t).keys())
        
                        