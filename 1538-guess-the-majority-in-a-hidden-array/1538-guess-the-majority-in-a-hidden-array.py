# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        eql,diff = 1,0
        diffIdx = -1
        
        def f(equal,i):
            nonlocal eql,diff,diffIdx
            if equal:
                eql+=1
            else:
                diff+=1
                diffIdx=i
        
        q0123 = reader.query(0,1,2,3)
        q1234 = reader.query(1,2,3,4)
        f(q1234==q0123,4)
        for i in range(5,n):
            f(reader.query(1,2,3,i)==q0123,i)
        f(reader.query(0,2,3,4)==q1234,1)
        f(reader.query(0,1,3,4)==q1234,2)
        f(reader.query(0,1,2,4)==q1234,3)
        # f(reader.query(0,1,2,))
        if eql==diff: return -1
        return 0 if eql>diff else diffIdx