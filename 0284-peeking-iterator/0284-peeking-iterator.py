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
    def __init__(self, iterator):
        self.iterator = iterator
        self.peekValue = None

    def peek(self):
        if self.peekValue is None:
            if not self.iterator.hasNext():
                raise StopIteration()
            self.peekValue = self.iterator.next()
        return self.peekValue

    def next(self):
        if self.peekValue is not None:
            value = self.peekValue
            self.peekValue = None
            return value
        if not self.iterator.hasNext():
            raise StopIteration()

        return self.iterator.next()

    def hasNext(self):
        return self.peekValue is not None or self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peekValue()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
