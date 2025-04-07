class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class MyQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        self.in_stack.push(x)

    def pop(self) -> int:
        if self.out_stack.isEmpty():
            while not self.in_stack.isEmpty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack.isEmpty():
            while not self.in_stack.isEmpty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def empty(self) -> bool:
        return self.in_stack.isEmpty() and self.out_stack.isEmpty()
