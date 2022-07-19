class Node:
    def __init__(self,place):
        self.place = place
        self.parent = None
        # self.children = []
    # def addChild(self,child):
    #     self.children.append
    # def __str__(self):
    #     return ("("+self.place+"=>"+(self.parent if self.parent!=None else "no parent")+")")
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], r1: str, r2: str) -> str:
        nodes = {}
        
        for reg in regions:
            parent,*children = reg
            
            if parent not in nodes:
                nodes[parent] = Node(parent)
            
            for child in children:
                if child not in nodes:
                    nodes[child] = Node(child)
                    nodes[child].parent = nodes[parent]
                # nodes[parent].addChild(nodes[child])
        seen = set()
        def lca(r1,r2):
            # print("printing r1,r2",r1,r2)
            temp = r1
            while temp:
                # print(temp,type(temp))
                seen.add(temp.place)
                temp = temp.parent
            temp = r2
            while temp:
                if temp.place in seen:
                    return temp.place
                temp = temp.parent
                
        # print(nodes)
        # for k in nodes:
        #     print(k,str(nodes[k]))
        # return ""
        return lca(nodes[r1],nodes[r2])
        # return 
        