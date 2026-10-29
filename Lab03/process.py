"""
Author: Preston Dahl
KUID: [ID REDACTED]
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Manages a single simulated process and its call stack of Function objects.
"""

from function import Function

class Process:
    def __init__(self, name):
        self.name = name
        self.is_running = True
        main_function = Function("main", False)
        self.call_stack.push(main_function)
        print(f"{self.name} process started")
    
    def call(self, function_name, can_handle):
        if not self.is_running:
            print(f"{self.name} process is over; CALL ignored")
            return
        func = Function(function_name, can_handle)
        self.call_stack.push(func)
        print(f"{self.name} calls {function_name} function")

    def raise_exception(self):
        if not self.is_running or self.call_stack.is_empty():
            print(f"{self.name} process is over; RAISE ignored")
            return

        raising_func = self.call_stack.pop()
        print(f"{self.name} has {raising_func.name} function raise exception")

        while not self.call_stack.is_empty():
            current_func = self.call_stack.peek()

            if current_func.can_handle_exceptions:
                print(f"{self.name} has {current_func.name} function handle exception")
                return
            else:
                popped = self.call_stack.pop()
                if popped.name == "main":
                    print(f"{self.name} process ended")
                    self.is_running = False
                    return
                else:
                    print(f"{self.name} pop {popped.name} function")
    def return_function(self):
        returned = self.call_stack.peek()
        if not self.is_running or self.call_stack.is_empty():
            print(f"{self.name} process is already over; RETURN ignored")
            return
            
        elif self.is_running and not self.call_stack.is_empty() and returned.name != "main":
            print(f"{self.name} has {returned.name} return")
            self.call_stack.pop()

        else:
            print(f"{self.name} has main return\n{self.name} process ending...")