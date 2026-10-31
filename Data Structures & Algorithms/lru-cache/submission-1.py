class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, lru_node:Node):
        prev_node = lru_node.prev
        next_node = lru_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_tail(self, node:Node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #Case when Key already exists
        
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.hash_map) == self.capacity:
                #Remove head and add new node to tail'
                lru_node = self.head.next
                self._remove(lru_node)
                del self.hash_map[lru_node.key]
            
            new_node = Node(key, value)
            self.hash_map[key] = new_node
            self._add_to_tail(new_node)