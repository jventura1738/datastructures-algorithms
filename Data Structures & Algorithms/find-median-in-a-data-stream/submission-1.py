from heapq import heappop, heappush, heappop_max, heappush_max


class MedianFinder:
    __slots__ = ("_min_heap", "_max_heap")
    def __init__(self):
        self._min_heap = []
        self._max_heap = []

    def addNum(self, num: int) -> None:
        if self._max_heap and num < self._max_heap[0]:
            heappush_max(self._max_heap, num)
        else:
            heappush(self._min_heap, num)
        
        # rebalance if necessary
        if len(self._max_heap) > len(self._min_heap) + 1:
            num = heappop_max(self._max_heap)
            heappush(self._min_heap, num)
        if len(self._min_heap) > len(self._max_heap) + 1:
            num = heappop(self._min_heap)
            heappush_max(self._max_heap, num)

    # 0 1 2   3 4 5
    def findMedian(self) -> float:
        if len(self._max_heap) > len(self._min_heap):
            return self._max_heap[0]
        if len(self._min_heap) > len(self._max_heap):
            return self._min_heap[0]
        return (self._max_heap[0] + self._min_heap[0]) / 2
        