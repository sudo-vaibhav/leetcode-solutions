class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        N = len(name)
        M = len(typed)
        while i<N and j<M:
            # get all of one type
            base_char = name[i]
            base_count= 0
            typed_count=0
            while i<N and name[i] == base_char:
                base_count+=1
                i+=1
            while j<M and typed[j] == base_char:
                typed_count+=1
                j+=1
            if base_count <= typed_count:
                pass
            else:
                return False
        
        return j>=M and i>=N