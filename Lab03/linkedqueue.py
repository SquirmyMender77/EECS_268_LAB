from node import Node
from stack import Stack

class linkedqueue:
    def __init__(self):
        self._front = None
        self._back = None
        self.stack = Stack
        self._length = 0

    def is_empty(self):
        if self._front == None:
            return True
        else:
            return False
        
    def __len__(self):
        return self._length
        
    def enqueue(self, entry):
        new = Node(entry)
        if self._back == None:
            self._back = new
            self._front = new
        elif self._back != None:
            self._back.next = new
            self._back = self._back.next
        self._length += 1

    def peek_front(self):
        if self._front != None:
            return self._front.entry
        else:
            print("the queue is empty")

    def dequeue(self):
        if self._front == None:
            print("nothing to dequeue")
            return None

        else:
            dequeued_data = self._front.entry
            self._front = self._front.next
            self._length -= 1
            if self._front == None:
                self._back = None
            return  dequeued_data

    def move_front(self):
        if self._front == None:
            print("cannot move front")
        else:
            temp = self._front
            self._back.next = temp
            self._front = self._front.next
