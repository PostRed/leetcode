class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # фиктивные переменные
        self.first = Node(0, 0)
        self.last = Node(0, 0)

        self.first.next = self.last
        self.last.prev = self.first

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # делаем node предпоследний
        node.prev = self.last.prev
        node.next = self.last
        node.prev.next = node
        self.last.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # обращаясь к элементу - делаем предпоследним, чтобы в начале остались элементы, к которым мало обращаются
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        # делаем элемент предпоследним
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            help = self.first.next
            self.remove(self.first.next)
            del self.cache[help.key]
