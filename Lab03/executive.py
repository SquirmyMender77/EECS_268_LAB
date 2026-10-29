"""
Author: Preston Dahl
KUID: [ID REDACTED]
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Reads commands from the input file and passes execution steps to Process.
"""

from process import Process

class Executive:
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        process = Process("math")
        try:
            with open(self.file_name, mode='r', encoding="utf-8") as f:
                for line in f:
                    if "START" in line:
                        pass
                    elif "CALL" in line:
                        for num in line:
                            process.call(num[2:3])
                    elif "RETURN" in line:
                        process.return_function()
                    elif "RAISE" in line:
                        process.raise_exception()
                    else:
                        print(f"invalid command: {line.strip()}")
        except FileNotFoundError:
            print(f"file '{self.file_name}' not found.")