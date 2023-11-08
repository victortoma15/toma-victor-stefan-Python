class Stack:
    def __init__ (self):
        self.stack = []

    def push (self, element):
        self.stack.append(element)

    def pop (self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def peek (self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def is_empty (self):
        if len(self.stack) == 0:
            return True
        else:
            return False


example_stack = Stack()
example_stack.push(15)
example_stack.push(17)
example_stack.push(29)
example_stack.push(10)
example_stack.push(16)
example_stack.push(22)
print(example_stack.pop())
print(example_stack.pop())
print(example_stack.stack)
print(example_stack.peek())
print(example_stack.is_empty())
