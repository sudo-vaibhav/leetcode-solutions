class Node:
    def __init__(self,key=inf,val=inf,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 0
    def __str__(self):
        return "(key="+str(self.key)+", val="+str(self.val)+")"
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sz = 0
        
    def remove(self,node):
        p,n = node.prev,node.next
        p.next = n
        n.prev = p
        node.prev = None
        node.next = None
        self.sz-=1
    def removeLast(self):
        if self.sz!=0:
            lastNode = self.tail.prev
            secondLast = lastNode.prev
            secondLast.next = self.tail
            self.tail.prev = secondLast
            lastNode.prev = None
            lastNode.next = None
            self.sz -= 1
            return lastNode
    
    def addFirst(self,node):
        oldFirstNode = self.head.next
        node.prev = self.head
        node.next = oldFirstNode
        oldFirstNode.prev = node
        self.head.next = node
        self.sz+=1            
            
    def __len__(self):
        return self.sz
    def __str__(self):
        ans = ""
        temp = self.head.next
        while temp!=self.tail:
            ans+= str(temp)+" "
            temp = temp.next
        return ans
class LFUCache:
    
    def show(self):
        print("minFreq: ",self.minFreq)
        print("DLL View")
        for k in self.freqDLL:
            if len(self.freqDLL[k])>0:print("freq:",k, "DLL:",self.freqDLL[k])
        print("DLL View end")
        print("freqNode view")
        for f in self.keyNode:
            print(f,self.keyNode[f])
        print("end freqNode view")
        
    def __init__(self, capacity: int):
        self.freqDLL = defaultdict(DLL)
        self.keyNode = {}
        self.cap = capacity
        self.usedCap = 0
        self.minFreq = 1
        
    def get(self, key: int) -> int:
        # print("op: get",key)
        # self.show()
        if key in self.keyNode:
            node = self.keyNode[key]
            freq = node.freq
            val = node.val
            self.freqDLL[freq].remove(node)
            if len(self.freqDLL[freq])==0 and freq==self.minFreq:
                self.minFreq+=1
            node.freq+=1
            self.freqDLL[freq+1].addFirst(node)
            return val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if self.cap<=0: return
        # print("op: put",key,value)
        # self.show()
        if key in self.keyNode:
            node = self.keyNode[key]
            self.freqDLL[node.freq].remove(node)
            if len(self.freqDLL[node.freq])==0 and node.freq==self.minFreq:
                self.minFreq+=1
        else:
            self.usedCap+=1
            if self.usedCap>self.cap:
                self.usedCap -= 1
                removedNode = self.freqDLL[self.minFreq].removeLast()
                del self.keyNode[removedNode.key]
                if len(self.freqDLL[self.minFreq])==0:
                    self.minFreq += 1
            node = Node(key=key,val=value)
            
        node.freq += 1
        node.val = value
        self.minFreq = min(self.minFreq,node.freq)
        self.freqDLL[node.freq].addFirst(node)
        self.keyNode[key]=node
        
