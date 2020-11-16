class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items


a = Stack()

a.push("A")
a.push("B")
a.push("C")
print(a.pop())
print(a.is_empty())
print(a.peek())
print(a.get_stack())
