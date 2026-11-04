class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k
        self.capacity = k
        self.front = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False

        index = (self.front + self.size) % self.capacity
        self.queue[index] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        index = (self.front + self.size - 1) % self.capacity
        return self.queue[index]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity