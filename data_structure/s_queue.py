from queue import Queue
import collections


class MaxQueue:
    def __init__(self):
        self.queue = Queue()
        self.deque = collections.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if self.queue.empty(): return -1
        val = self.queue.get()
        if val == self.deque[0]:
            self.deque.popleft()
        return val


if __name__ == "__main__":

    maxque = MaxQueue()
    print(maxque.push_back(1))
    print(maxque.push_back(2))
    print(maxque.max_value())
    print(maxque.pop_front())
    print(maxque.max_value())
