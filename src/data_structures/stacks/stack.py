"""
@Author  : luo-songtao
"""

class StackOverflowError(BaseException):
    pass

class StackUnderflowError(BaseException):
    pass


class Stack:

    def __init__(self, limit=10):
        self.limit = limit
        self.stack = []
        self.top = -1

    def push(self, x):
        if self.size >= self.limit:
            raise StackOverflowError
        else:
            self.stack.append(x)
            self.top += 1

    def pop(self):
        if self.top == -1:
            raise StackUnderflowError
        else:
            x = self.stack.pop()
            self.top -= 1
            return x

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    @property
    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack(10)
    assert stack.is_empty() is True, "stack is not empty"
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.size == 2
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
