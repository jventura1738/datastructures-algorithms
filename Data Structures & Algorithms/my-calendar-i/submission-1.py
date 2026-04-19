from sortedcontainers import SortedList
from bisect import bisect_left


class MyCalendar:
    __slots__ = ("_bookings",)

    def __init__(self):
        self._bookings = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        insertion_idx = self._bookings.bisect_left((startTime, endTime))

        # bisect left tells us that at least startTime < start.
        # so now look back that prev end does not overlap
        if insertion_idx > 0 and self._bookings[insertion_idx -1][1] > startTime:
            return False
        
        # now check that our end does not overlap with next start
        if insertion_idx < len(self._bookings) and self._bookings[insertion_idx][0] < endTime:
            return False
        
        self._bookings.add((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)