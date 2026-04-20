from random import randint


class RandomizedSet:
    __slots__ = ("_list", "_size", "_val_idx_map")

    def __init__(self):
        self._list = []
        self._size = 0
        self._val_idx_map = defaultdict(lambda: -1)

    def insert(self, val: int) -> bool:
        if self._val_idx_map[val] != -1:
            return False
        
        self._val_idx_map[val] = self._size
        self._list.append(val)
        self._size += 1
        return True

    def remove(self, val: int) -> bool:
        if self._val_idx_map[val] == -1:
            return False

        idx = self._val_idx_map[val]
        last_idx = self._size - 1
        last_val = self._list[last_idx]

        # Move last element into idx slot if we're not removing the last one
        if idx != last_idx:
            self._list[idx] = last_val
            self._val_idx_map[last_val] = idx

        self._list.pop()
        self._size -= 1
        self._val_idx_map[val] = -1
        return True

    def getRandom(self) -> int:
        idx = randint(0, self._size - 1)
        return self._list[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()