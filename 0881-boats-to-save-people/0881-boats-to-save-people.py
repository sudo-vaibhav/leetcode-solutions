class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i,j = 0,n-1
        ans = 0
        while i<=j:
            cur = people[j]
            if i!=j and people[i]+cur<=limit:
                i+=1
            ans += 1
            j-=1
        
        return ans