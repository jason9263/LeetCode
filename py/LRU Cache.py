class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.dic = dict()
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = Node(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = headNext
        headNext.pre = node

    def removeFromTail(self):
        if len(self.dic) == 0:
            return
        tail_node = self.tail.pre
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
