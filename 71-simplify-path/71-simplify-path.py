class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split("/")
        # print(folders)
        res = []
        for folder in folders:
            if folder:
                if folder == ".":
                    pass
                elif folder == "..":
                    if len(res)>0:res.pop()
                else:
                    res.append(folder)
        # print(res)
        return "/"+"/".join(res)