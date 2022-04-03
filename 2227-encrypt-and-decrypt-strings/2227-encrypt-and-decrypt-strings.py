class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keyVal = {}
        self.d =set()
        for w in dictionary:
            self.d.add(w)
        for i in range(len(keys)):
            self.keyVal[keys[i]]=values[i]
        
    @cache
    def encrypt(self, word1: str) -> str:
        ans = ""
        for c in word1:
            ans+= self.keyVal[c]
        return ans

    @cache
    def decrypt(self, word2: str) -> int:
        ans = 0
        for w in self.d:
            if len(word2)==2*len(w):
                for idx,c in enumerate(w):
                    if self.keyVal[c]==word2[2*idx:2*idx+2]:
                        continue
                    else:
                        break
                else:
                    ans+=1
        return ans