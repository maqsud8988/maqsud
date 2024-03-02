# #### Queue
#
#
#
#
#
# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         else:
#             return "Queue bo'sh"
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#
#
#
#
#
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(queue.dequeue())
#
#
#
#
#
#
#
# ### stac
#
#
#
#
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return "Stack bo'sh"
#
#     def peek(self):
#         return self.stack[-1] if not self.is_empty() else "Stack bo'sh"
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#
#
#
#
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())
# print(stack.peek())
#
#
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print ("Eror: Stack is empty")
#
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             print("Eror: Stack is empty")
#
#
#     def size(self):
#         return  len(self.items)
#
#
#
#
#
#
# stack = Stack()
#
#
# stack.push(23)
# stack.push(1)
# stack.push(2)
# print(stack.items)
# stack.size()
# stack.pop()
# print(stack.size())
# print(stack.items)
# print(stack.pop())
#
#
#
# for i in stack.items:
#     print(i)
