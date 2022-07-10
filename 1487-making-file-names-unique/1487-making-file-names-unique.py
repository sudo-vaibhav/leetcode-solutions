class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        usedNames = set()
        nameCount = defaultdict(int)
        
        ans = []
        for name in names:
            origName = name
            # if "(" in name:
            #     cnt = int(re.findall(r"\d+",name)[0])
            #     name = re.findall(r"(.+)\(",name)[0]
            # else:
            #     cnt = 0
            # print(name,cnt)  
            actual = nameCount[name]
            i = actual
            if origName not in usedNames:
                ans.append(origName)
                usedNames.add(origName)
            else:
                while True:
                    newName = name
                    if actual!=0:
                        newName += "("+str(actual)+")"
                    if newName not in usedNames:
                        ans.append(newName)
                        usedNames.add(newName)
                        break
                    actual+=1
                nameCount[name] = actual
            
        return ans