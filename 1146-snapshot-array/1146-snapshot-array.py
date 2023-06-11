from sortedcontainers import SortedSet
class SnapshotArray:
    
    
    def __init__(self, length: int):
        self.affected = set()
        self.arr = defaultdict(lambda:defaultdict(int))
        self.snaps = defaultdict(SortedSet)
        self.curSnap = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.curSnap]=val
        self.affected.add(index)
    def snap(self) -> int:
        
        for index in self.affected:
            self.snaps[index].add(self.curSnap)
        self.affected = set()
        self.curSnap+=1
        return self.curSnap-1

    def get(self, index: int, snap_id: int) -> int:
        try:
            if snap_id in self.snaps[index]:
                return self.arr[index][snap_id]
            # print(self.snaps[index])
            last_snap = bisect_left(self.snaps[index],snap_id)
            if last_snap==len(self.snaps[index]):
                return self.arr[index][self.snaps[index][last_snap-1]]
            elif last_snap==0: return 0
            else:
                
                val = self.snaps[index][last_snap-1]
                return self.arr[index][val]
#             if val>snap_id: return 0
            
#             print(last_snap,index,snap_id)
            # print(last_snap)
            
        except:
            return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)