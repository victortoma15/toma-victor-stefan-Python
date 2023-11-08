class Queue:
    def __init__ (self):
        self.queue = []

    def push (self, element):
        self.queue.append(element)

    def pop (self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def peek (self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    def is_empty (self):
        if len(self.queue) == 0:
            return True
        else:
            return False


example_queue = Queue()
example_queue.push(15)
example_queue.push(17)
example_queue.push(29)
example_queue.push(10)
example_queue.push(16)
example_queue.push(22)
print(example_queue.pop())
print(example_queue.pop())
print(example_queue.queue)
print(example_queue.peek())
print(example_queue.is_empty())
