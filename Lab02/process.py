"""
Author: Preston Dahl
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Manages a single simulated process and its call stack of Function objects.
"""

from stack import Stack
from function import Function
from linkedqueue import linkedqueue

class ProcessState:
    def __init__(self, name):
        self.name = name
        self.call_stack = Stack()
        self.is_running = True

class Process:
    def __init__(self):
        self.linked = linkedqueue()

    def start(self, name):
        new_process = ProcessState(name)
        main_function = Function("main", False)
        new_process.call_stack.push(main_function)
        self.linked.enqueue(new_process)
    
    def call(self, function_name, can_handle):
        active = self.linked.peek_front()

        if not active.is_running:
            print(f"{active.name} process is over; CALL ignored")
            return
        func = Function(function_name, can_handle)
        active.call_stack.push(func)
        print(f"{active.name} calls {function_name}")
        self.linked.move_front()

    def raise_exception(self):
        active = self.linked.peek_front()
        if not active.is_running or active.call_stack.is_empty():
            print(f"{active.name} process is over; RAISE ignored")
            return

        raising_func = active.call_stack.pop()
        print(f"{active.name} has {raising_func.name} raise exception")

        while not active.call_stack.is_empty():
            current_func = active.call_stack.peek()

            if current_func.can_handle_exceptions:
                print(f"{active.name} has {current_func.name} handle exception")
                return
            else:
                popped = active.call_stack.pop()
                if popped.name == "main":
                    print(f"{active.name} process ended")
                    active.is_running = False
                    return
                else:
                    print(f"{active.linked.peek_front()} pop {popped.name} function")
    def return_function(self):
        active = self.linked.peek_front()
        returned = active.call_stack.peek()
        if not active.is_running or active.call_stack.is_empty():
            print(f"{active.name} process is already over; RETURN ignored")
            return
            
        elif active.is_running and not active.call_stack.is_empty() and returned.name != "main":
            print(f"{active.name} has {returned.name} return")
            active.call_stack.pop()

        else:
            print(f"{active.name} has main return\n{active.name} process ending...")
            active.call_stack.pop()
            if not active.is_running or active.call_stack.is_empty():
                self.linked.dequeue()
                if self.linked.is_empty() or self.linked.peek_front() == None:
                    print("nothing left to return")