import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    # @abstractmethod
    # define your fields here
    def __init__(self,val,op,left=None,right=None):
        self.val = val
        self.op = op
        self.left = left
        self.right = right
        
    def evaluate(self) -> int:
        if not self.op:return self.val
        else:
            L,R = self.left.evaluate(),self.right.evaluate()
            if self.op:
                if self.val == "+":
                    return L+R
                elif self.val == "-":
                    return L-R
                elif self.val == "*":
                    return L*R
                else:
                    return L//R
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        st = deque()
        for cur in postfix:
            if cur in "+*/-":
                right,left = st.pop(),st.pop() 
                node = Node(cur,True,left,right)
            else:
                node = Node(int(cur),False)
            st.append(node)
        
        return st[-1]
            
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        