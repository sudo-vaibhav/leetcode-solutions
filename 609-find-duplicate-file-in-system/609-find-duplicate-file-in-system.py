class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            path,*files = path.split(" ")
            
            for file in files:
                fileName,content = file.split("(")
                content = content[:-1]
                d[content].append(path+"/"+fileName)
        
        return [x for x in d.values() if len(x)>1]