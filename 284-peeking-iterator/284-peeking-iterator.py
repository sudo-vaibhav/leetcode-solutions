# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, it):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = it
        self.buf = collections.deque()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.buf:
            self.buf.append(self.it.next())    
        return self.buf[0] 
        

    def next(self):
        """
        :rtype: int
        """
        if not self.buf:
            self.buf.append(self.it.next())
        return self.buf.popleft()
        

    def hasNext(self):
        return len(self.buf)>0 or self.it.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].