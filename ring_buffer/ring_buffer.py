class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # capacity = []
        self.storage = []
        self.writePointer = 0
        for i in range(self.capacity):
            self.storage.append(None)

    def append(self, item):
        self.storage[self.writePointer] = item
        self.writePointer += 1
        if self.writePointer == self.capacity:  # self.writePointer >= self.capacity
            self.writePointer = 0  # self.writePointer = self.writePointer % self.capacity(self.writePointer index = 0)

    def get(self):
        rv = []
        for item in self.storage:
            if item is not None:
                rv.append(item)
        return rv
    
    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return f'Data in the Ringbuffer: {self.storage}'


buffer = RingBuffer(10)
print(buffer)
print(len(buffer))
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.get())
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.append('j')
buffer.append('k')
print(buffer.get())
