class Stack:
    items = []

    def stack_push(self, item):
        self.items.append(item)

    def stack_pop(self):
        self.items.pop()

    def stack_len(self):
        return len(self.items)

    def stack_print(self):
        print(self.items)


stack_obj = Stack()
stack_obj.stack_push(5)
stack_obj.stack_push(8)
stack_obj.stack_push(3)
print(stack_obj.stack_len())
stack_obj.stack_pop()

stack_obj.stack_print()
