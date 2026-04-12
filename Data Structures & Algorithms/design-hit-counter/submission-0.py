from collections import deque

class HitCounter:

    def __init__(self):
        self._queue = deque()

    def hit(self, timestamp: int) -> None:
        self._queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self._queue:
            if timestamp - self._queue[0] >= (5 * 60):
                self._queue.popleft()
            else:
                break
        return len(self._queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
