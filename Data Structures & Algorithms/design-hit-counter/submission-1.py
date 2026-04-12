from collections import deque

class HitCounter:

    def __init__(self):
        self._queue = deque()

    def hit(self, timestamp: int) -> None:
        self._queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        window_start = timestamp - (5 * 60)
        while self._queue and self._queue[0] <= window_start:
            self._queue.popleft()
        return len(self._queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
