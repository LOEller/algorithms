class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def getNodeAtIndex(self, index):
        node = self.head
        idx = 0
        while node:
            if idx == index:
                return node
            node = node.next
            idx += 1

    def get(self, index: int) -> int:
        if node := self.getNodeAtIndex(index):
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.length += 1
        new_node = Node(val=val, prev=None, next=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        self.length += 1
        new_node = Node(val=val, prev=self.tail, next=None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return # do nothing
        elif index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            self.length += 1
            # we are adding to the middle of the list
            node = self.getNodeAtIndex(index)
            new_node = Node(val=val, prev=node.prev, next=node)
            node.prev.next = new_node
            node.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return # do nothing
        elif index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # we are deleting a node in the middle of the list
            node = self.getNodeAtIndex(index)
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1


