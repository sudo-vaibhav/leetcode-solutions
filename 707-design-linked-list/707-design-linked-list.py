class Node:
    def __init__(self,data,pre=None,nex=None):
        self.val=data
        self.prev = pre
        self.next = nex

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def pl(self):
        return
        temp = self.head
        print("printing list")
        while temp:
            print(temp.val,end=",")
            temp=temp.next
        print()
        print("length",self.length)
    def get(self, index: int) -> int:
        if index>=self.length or index<0:
            return -1
        temp = self.head
        k = 0
        while k!=index:
            temp = temp.next
            k+=1
        return temp.val

    def addAtHead(self, val: int) -> None:
        self.pl()
        newNode = Node(val)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode
        if self.length==0:
            self.tail = self.head
        self.length+=1

    def addAtTail(self, val: int) -> None:
        self.pl()
        newNode = Node(val)
        newNode.prev = self.tail
        if self.tail:
            self.tail.next = newNode
        self.tail = newNode
        if self.length==0:
            self.head = self.tail
        self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        self.pl()
        if index<0: return
        elif index>self.length: return
        elif index==0:
            self.addAtHead(val)
        elif index==self.length:
            self.addAtTail(val)
        else:
            k = 0
            temp = self.head
            while k!=index-1:
                temp = temp.next
                k+=1
            newNode = Node(val)
            newNode.next = temp.next
            temp.next = newNode
            if newNode.next:
                newNode.next.prev = newNode
            newNode.prev = temp
            self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        self.pl()
        if index<0 or index>=self.length: return
        if index==self.length-1:
            self.tail = self.tail.prev
        k = 0
        temp = self.head
        while k!=index:
            k+=1
            temp = temp.next
        pre,nex = temp.prev,temp.next
        if pre:
            pre.next = nex
        if nex:
            nex.prev = pre
        self.length-=1
        if index==0:
            self.head = self.head.next
        if self.length==0:
            self.head,self.tail = None,None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)