class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, element):
        self.queue.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)


class MyStack:

    def __init__(self):
        self.queue_in = Queue()
        self.queue_out = Queue()

    def push(self, x: int) -> None:
        self.queue_out.push(x)
        while not self.queue_in.isEmpty():
            self.queue_out.push(self.queue_in.pop())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in

    def pop(self) -> int:
        return self.queue_in.pop()

    def top(self) -> int:
        return self.queue_in.peek()

    def empty(self) -> bool:
        return self.queue_in.isEmpty()
