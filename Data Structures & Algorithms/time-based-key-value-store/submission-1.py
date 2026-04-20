from bisect import bisect_right


class TimeMap:
    __slots__ = ("_store", )
    def __init__(self):
        self._store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        history = self._store[key]
        if not history:
            return ""
        idx = bisect_right(history, timestamp, key=lambda t: t[0]) - 1
        if idx < 0:
            return ""
        return history[idx][1]
