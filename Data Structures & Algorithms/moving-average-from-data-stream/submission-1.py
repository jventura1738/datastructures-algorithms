from collections import deque

class MovingAverage:
    __slots__ = ("_size", "_queue", "_sum")
    def __init__(self, size: int):
        self._size = size
        self._queue = deque()
        self._sum = 0

    def next(self, val: int) -> float:
        self._queue.append(val)
        self._sum += val

        # if window exceeds, pop
        if len(self._queue) > self._size:
            remove_me = self._queue.popleft()
            self._sum -= remove_me
        
        window_size = min(len(self._queue), self._size)
        ans = self._sum / window_size
        return ans


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
