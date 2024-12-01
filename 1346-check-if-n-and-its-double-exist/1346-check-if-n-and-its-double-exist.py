class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # c = defaultdict(int)
        s = set(arr)
        if(Counter(arr)[0]>1): return True
        for num in set(arr):
            if num!=0:
                if num*2 in s:
                    return True
                if num%2==0 and num//2 in s:
                    return True
        return False