class Node:
    def __init__(self,name="",fsType="dir",content=""):
        self.name = name
        self.type = fsType
        self.content = content
        self.children = dict()
        
class FileSystem:

    def __init__(self):
        self.root = Node()
    
    def chunkedPath(self,path):
        return path.split("/")[1:]
    
    def ls(self, path: str) -> List[str]:
        orig = path
        path = self.chunkedPath(path)
        
        def recurse(idx,node):
            if idx==len(path) or path[idx]=="":
                if node.type=="file":
                    return [node.name]
                return sorted(node.children.keys())
            else:
                cur = path[idx]
                return recurse(idx+1,node.children[cur])
        
        return recurse(0,self.root)

    def mkdir(self, path: str) -> None:
        path = self.chunkedPath(path)
        self.chunkedmkdir(path)
        
    def chunkedmkdir(self,path):
        def recurse(idx,node):
            if idx>=len(path):return
            cur = path[idx]
            if cur in node.children:
                pass
            else:
                node.children[cur] = Node(cur)
            recurse(idx+1,node.children[cur])
                
        recurse(0,self.root)

        
    def addContentToFile(self, filePath: str, content: str) -> None:
        path = self.chunkedPath(filePath)
        self.chunkedmkdir(path[:-1])
        
        def recurse(idx,node):
            if idx==len(path):
                node.content += content                
            else:
                cur = path[idx]
                if idx==len(path)-1 and cur not in node.children:
                    node.children[cur] = Node(cur,"file")
                recurse(idx+1,node.children[cur])
                
            
        recurse(0,self.root)

    def readContentFromFile(self, filePath: str) -> str:
        path = self.chunkedPath(filePath)
        
        def recurse(idx,node):
            if idx==len(path):
                return node.content
            else:
                cur = path[idx]
                return recurse(idx+1,node.children[cur])
                
            
        return recurse(0,self.root)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)