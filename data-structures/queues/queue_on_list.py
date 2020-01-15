"""
@Author  : luo-songtao
"""

class QueueEmptyError(BaseException):
    pass


class QueueFullError(BaseException):
    pass


class Queue:

    def __init__(self, limit=10):
        self.limit = limit
        self.queue = []
        
    def put(self, x):
        if self.is_full():
            raise QueueFullError
        self.queue.append(x)
    
    def get(self):
        if self.is_empty():
            raise QueueEmptyError
        return self.queue.pop(0)
    
    def is_full(self):
        return False if self.size < self.limit else False    
    
    def is_empty(self):
        return True if self.size == 0 else False
    
    @property
    def size(self):
        return len(self.queue)
    
    
if __name__ == "__main__":
    queue = Queue()

    queue.put(1)
    queue.put(2)
    queue.put(3)
    assert queue.get() == 1
    assert queue.is_full() is False
    
    queue.get()
    queue.get()
    assert queue.is_empty() is True
    queue.get()