class Queue:
    items = []

    def inqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def queue_print(self):
        print(self.items)

    def queue_len(self):
        return len(self.items)


queue_obj = Queue()
queue_obj.inqueue(3)
queue_obj.inqueue(5)
queue_obj.inqueue(2)
queue_obj.inqueue(8)

queue_obj.queue_print()
print(queue_obj.queue_len())

queue_obj.dequeue()

queue_obj.queue_print()
print(queue_obj.queue_len())
