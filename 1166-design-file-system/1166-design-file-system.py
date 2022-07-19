VAL = "##"
class FileSystem:

    def __init__(self):
        self.root = {}
    def createPath(self, path: str, value: int) -> bool:
        subparts = path[1:].split("/")
        pathToFinal = subparts[:-1]
        finalName = subparts[-1]
        temp = self.root
        for name in pathToFinal:
            if name not in temp:
                return False
            temp = temp[name]
        
        if finalName in temp:
            return False
        temp[finalName] = {VAL:value}
        return True
    def get(self, path: str) -> int:
        subparts = path[1:].split("/")
        temp = self.root
        
        for idx,name in enumerate(subparts):
            if name not in temp:
                return -1
            temp = temp[name]
        # print(str(temp)[0])
        if VAL not in temp:
            return -1
        return temp[VAL]
