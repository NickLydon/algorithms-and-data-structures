class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def rev_string(sample):
    forwards = Stack()
    for s in sample:
        forwards.push(s)
    reversed = ""
    while not forwards.isEmpty():
        reversed += forwards.pop()

    return reversed


def parens_balances(parens):
    left = Stack()
    for p in parens:
        if p == "(":
            left.push(p)
        elif p == ")" and not left.isEmpty():
            left.pop()
        else:
            return False

    return left.isEmpty()


print(parens_balances("((()))"))