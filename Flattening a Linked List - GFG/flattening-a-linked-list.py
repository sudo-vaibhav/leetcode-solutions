#User function Template for python3

from heapq import heappush,heappop



def flatten(root):
    pointers = []
    
    temp = root
    dummy = Node(0)
    i=0
    while temp:
        heappush(pointers,(temp.data,i,temp))    
        temp = temp.next
        i+=1
        
    temp = dummy
    
    while pointers:
        cur,_,curNode = heappop(pointers)
        temp.bottom = curNode
        temp = curNode
        nex = curNode.bottom
        if nex!=None:
            heappush(pointers,(nex.data,i,nex))
            i+=1
        curNode.bottom = None
    
    return dummy.bottom
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends