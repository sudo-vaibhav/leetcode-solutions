class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        st = deque()
        def getMap(word):
            ans = [0]*26
            for i in word:
                ans[ord(i)-ord('a')]+=1
            return ans
        
        i = len(words)-1
        for word in words[::-1]:
            temp = getMap(word)
            while st and st[-1][1]==temp:
                st.pop()
            st.append((i,temp))
            i-=1
        # print(st)
        return [words[s[0]] for  s in st][::-1]
        
                