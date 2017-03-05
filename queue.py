class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data


class DeQueue:
    def __init__(self):
        self.items = []
        self.head = None
        self.tail = None
        self.len = 0

    def isEmpty(self):
        return self.head == None

    def enqueueFront(self, item):
        if self.isEmpty():
            self.enqueueRear(item)
        else:
            node = Node(item)
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
            self.len += 1

    def dequeueRear(self):
        data = self.tail.get_data()
        self.tail = self.tail.get_prev()
        self.len -= 1
        if self.len == 0:
            self.head = None
            self.tail = None
        return data

    def enqueueRear(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node
        self.len += 1

    def dequeueFront(self):
        node = self.head
        self.len -= 1
        self.head = self.head.get_next()
        if self.len == 0:
            self.tail = None
            self.head = None
        return node.get_data()

    def peek(self):
        return self.head.get_data()

    def size(self):
        return self.len


q = DeQueue()
for i in range(0, 10):
    q.enqueueRear(i)

while not q.isEmpty():
    print(q.dequeueFront())


def palindrome(s1):
    d = DeQueue()
    for s in s1:
        d.enqueueRear(s)

    while d.size() > 1:
        if d.dequeueFront() != d.dequeueRear():
            return False

    return True


print(palindrome("oa"))