class DLLNode{
    public DLLNode prev,nex;
    public int val,key;
    public DLLNode(int key, int val){
        this.key = key;
        this.val = val;
        this.prev = null;
        this.nex = null;
    }
}

class DLL{
    DLLNode head,tail;
    int sz;
    public DLL(){
        head = new DLLNode(-1,-1);
        tail = new DLLNode(-1,-1);
        head.nex = tail;
        tail.prev = head;
        sz=0;
    }
    
    public void moveToBack(DLLNode node){
        var previousNode = node.prev;
        var nextNode = node.nex;
        previousNode.nex = nextNode;
        nextNode.prev = previousNode;
        this.append(node);
        sz--; // to balance the effect of appending on size
    }
    
    public void append(DLLNode node){
        node.prev = tail.prev;
        node.nex = tail;
        tail.prev.nex = node;
        tail.prev = node;
        sz++;
    }
    public int size(){
        return sz;
    }
    public DLLNode popfront(){
        if (this.size()>0){
            var toBeDeleted = head.nex;
            head.nex = toBeDeleted.nex;
            toBeDeleted.nex.prev = head;
            sz--;
            return toBeDeleted;
        }
        return null;
    }
}
class LRUCache {
    int cap;
    HashMap<Integer,DLLNode> hm;
    DLL dll;
    public LRUCache(int capacity) {
        cap = capacity;
        dll = new DLL();
        hm = new HashMap<Integer,DLLNode>();
    }
    
    public int get(int key) {
        if (cap==0 || !hm.containsKey(key)){
            return -1;
        }
        var node = hm.get(key);
        dll.moveToBack(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if(hm.containsKey(key)){
            var node = hm.get(key);
            node.val = value;
            dll.moveToBack(node);
        }
        else{
            var newNode = new DLLNode(key,value);
            dll.append(newNode);
            hm.put(key,newNode);
        }
        if (dll.size()>cap){
            var deletedNode = dll.popfront();
            hm.remove(deletedNode.key);            
        }
    }
}

// potential improvement, outsource hashmap control to DLL itself

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */