class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        seen = set()
        
        for word in words:
            cur = ""
            for c in word:
                pos = ord(c)-ord("a")
                cur += chars[pos]
            seen.add(cur)
        
        return len(seen)