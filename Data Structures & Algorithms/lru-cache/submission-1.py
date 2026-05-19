class Node:
    def __init__(
        self,
        key: int,
        val: int,
    ) -> None:
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self._cap = capacity
        self._map = {}
        self._head = Node(0, 0)
        self._tail = Node(0, 0)
        self._head.nxt = self._tail
        self._tail.prv = self._head
    
    def _remove(self, node: Node) -> None:
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv
    
    def _append(self, node: Node) -> None:
        actual_tail = self._tail.prv
        actual_tail.nxt = node
        self._tail.prv = node
        node.nxt = self._tail
        node.prv = actual_tail

    def get(self, key: int) -> int:
        if key in self._map:
            self._remove(self._map[key])
            self._append(self._map[key])
            return self._map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self._remove(self._map[key])
        self._map[key] = Node(key, value)
        self._append(self._map[key])

        if len(self._map) > self._cap:
            lru_node = self._head.nxt
            self._remove(lru_node)
            del self._map[lru_node.key]
