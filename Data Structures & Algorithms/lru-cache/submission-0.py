class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.hash_map:
            return self.hash_map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #Case when Key already exists
        
        if key in self.hash_map:
            self.hash_map[key].val = value
        else:
            new_node = Node(key, value)
            if len(self.hash_map) == self.capacity:
                #Remove head and add new node to tail
                self.hash_map.pop(self.head.key)
                self.head = self.head.next
                self.tail.next = new_node
                self.tail = new_node
                self.hash_map[key] = new_node
                
            else:
                if not self.head:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                self.hash_map[key] = new_node
