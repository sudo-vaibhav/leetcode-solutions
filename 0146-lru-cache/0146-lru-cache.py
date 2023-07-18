# print("hello",cacheinstance)
class ListNode:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
    def __str__(self):
        return "<"+str(self.val)+">"
class DLL:
    def __init__(self):
        self.newest = ListNode(-1,-1)
        self.oldest = ListNode(-1,-1)
        self.newest.next = self.oldest
        self.oldest.prev = self.newest
        self.size = 0
    def remove_oldest(self,cacheinstance):
        del cacheinstance.key_to_node[self.oldest.prev.key]
        self.oldest.prev.prev.next = self.oldest
        self.oldest.prev = self.oldest.prev.prev
        self.size -= 1
    def __str__(self):
        ans = "["
        temp = self.newest.next
        while temp.key!=-1:
            ans += str(temp)
            temp = temp.next
        ans += "]"
        return ans
    def add(self,node,cacheinstance):
        old_prev = node.prev
        old_next = node.next
        if old_prev:
            old_prev.next = old_next
        if old_next:
            old_next.prev = old_prev
        node.next = self.newest.next
        node.prev = self.newest
        self.newest.next.prev = node
        self.newest.next = node
        self.size+=1
        
class LRUCache: 
            
    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.cap = capacity
        self.used_cap = 0
        self.ll = DLL()
        
    def get(self, key: int) -> int:
        # print("get",key,self.ll)
        if key not in self.key_to_node: return -1        
        self.ll.add(self.key_to_node[key],self)
        # self.key_to_freq[key]+=1
        return self.key_to_node[key].val

    def put(self, key: int, value: int) -> None:
        # print("put",key,value,self.ll)
        if key not in self.key_to_node:
            if self.used_cap == self.cap:
                self.ll.remove_oldest(self)
                self.used_cap -= 1
            self.key_to_node[key] = ListNode(key,-1)
            # self.key_to_freq[key] = 0
            self.used_cap += 1
        self.key_to_node[key].val = value
        self.ll.add(self.key_to_node[key],self)
        # self.key_to_freq[key]+=1
        # self.lowest_freq = min(self.lowest_freq,self.key_to_freq[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)