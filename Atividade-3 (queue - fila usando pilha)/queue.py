from stack import SinglyLinkedList

class Queue:
    def __init__(self):
        self.tmp_queue = SinglyLinkedList()
        self.queue = SinglyLinkedList()
    
    def enqueue(self, val):
        while not self.is_empty():
            self.tmp_queue.insert_at_top(self.queue.delete_from_top())
        
        self.queue.insert_at_top(val)
        
        while not self.tmp_queue.is_empty():
            self.queue.insert_at_top(self.tmp_queue.delete_from_top())

    def dequeue(self):
        if self.is_empty():
            raise Exception("A fila está vazia!")
        
        return self.queue.delete_from_top()
    
    def is_empty(self):
        return self.queue.is_empty()

### Testes

queue = Queue()

print(queue.is_empty()) # True

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(8)

print(queue.is_empty()) # False

print(queue.dequeue()) # 1
print(queue.dequeue()) # 2
print(queue.dequeue()) # 4
print(queue.dequeue()) # 8

print(queue.is_empty()) # True

queue.dequeue() # Exception("A fila está vazia!")