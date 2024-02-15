class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        rsi,rei = toBeRemoved
        
        def compute(interval):
            si,ei = interval
            if rsi<=si<ei<=rei:
                return []
            if ei<=rsi:
                return [(si,ei)]
            if rei<=si:
                return [(si,ei)]
            if si<rsi and ei>rei:
                return [(si,rsi),(rei,ei)]
            if ei<=rei:
                return [(si,rsi)]
            return [(rei,ei)]
        
        for interval in intervals:
            ans.extend(compute(interval))
        return ans