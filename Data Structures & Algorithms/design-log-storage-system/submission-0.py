from sortedcontainers import SortedList

class LogSystem:
    __slots__ = ("_logs", )
    def __init__(self):
        self._logs = SortedList()

    def put(self, log_id: int, timestamp: str) -> None:
        self._logs.add((timestamp, log_id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        cuts = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }
        ans = []
        for ts, log_id in self._logs:
            gran = cuts[granularity]
            if start[:gran] <= ts[:gran] <= end[:gran]:
                ans.append(log_id)
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
