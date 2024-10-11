from sortedcontainers import SortedSet
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        by_arrivals = sorted(zip(range(len(times)),times),key=lambda x:x[1][0])
        ac = SortedSet([i for i in range(0,len(times))])
        occupied = SortedSet()
        for idx,(arrival,leaving) in by_arrivals:
            while occupied and occupied[0][0]<=arrival:
                elem = occupied[0]
                _,seat_freed = elem
                occupied.remove(elem)
                ac.add(seat_freed)
            lowest_seat = ac[0]
            occupied.add((leaving,lowest_seat))
            ac.remove(lowest_seat)
            
            if targetFriend==idx:
                return lowest_seat