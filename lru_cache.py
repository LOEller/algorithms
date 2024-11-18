class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key # store reference to key so it can be deleted
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.cache = {}
        self.head = None # indicates the LRU item in the cache
        self.tail = None # indicates the MRU item in the cache

    def deleteHead(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def moveNodeToTail(self, node):
        if node == self.tail:
            return

        # handle is node being moved is the head
        if node == self.head:
            self.head = node.next

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # node is moved to tail end of list
        node.prev = self.tail
        node.next = None
        if self.tail:
            self.tail.next = node
        self.tail = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # the list node represented by self.cache[key] becomes the new 
            # tail indicating it is now the most recently used item
            node = self.cache[key]
            self.moveNodeToTail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update existing node and move it to tail
            node = self.cache[key]
            node.val = value
            self.moveNodeToTail(node)
        else:
            # an new node is added to the tail end of list
            node = Node(key=key, val=value, prev=self.tail, next=None)
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            # the key is added to the dictionary
            self.cache[key] = node

            self.length += 1
            if self.length > self.capacity:
                del self.cache[self.head.key]
                self.deleteHead()
                self.length -= 1


        
        


