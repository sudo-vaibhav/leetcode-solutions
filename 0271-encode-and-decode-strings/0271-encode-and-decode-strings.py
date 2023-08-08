class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(map(lambda x:"_".join(x),map(lambda x:(str(len(x)),x),strs)))
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        ans = []
        while i<len(s):
            j = i
            while j<len(s):
                if s[j]=="_":
                    break
                j+=1
            count = int(s[i:j])
            k = j+1
            cur = ""
            while count>0:
                cur += s[k]
                k+=1
                count-=1
            ans.append(cur)
            i = k
        
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))