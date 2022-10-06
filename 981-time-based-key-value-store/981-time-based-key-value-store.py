from sortedcontainers import SortedSet
class TimeMap:

    def __init__(self):
        self.keyTime = defaultdict(SortedSet)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTime[key].add((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        temp = self.keyTime[key]
        # print("temp",temp,key,timestamp)
        if len(temp)==0:return ""
        idx = bisect_left(temp,(timestamp,""))
        # print(idx)
        if idx==len(temp):
            return temp[idx-1][1]
        else:
            if temp[idx][0]>timestamp:
                if idx==0:
                    return ""
                return  temp[idx-1][1]
            return temp[idx][1]
        # if temp[idx][0]==timestamp:
        #     print("here")
        #     return temp[idx][1]
        # else:
        #     if idx-1==-1:
        #         return ""
        #     else:
        #         return temp[idx-1][1]
        # print(idx)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)