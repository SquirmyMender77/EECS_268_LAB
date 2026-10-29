"""
Author: Preston Dahl
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Reads commands from the input file and passes execution steps to Process.
"""

from process import Process

class Processor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.process = Process()
    def run(self):
        try:
            with open(self.file_name, mode = 'r', encoding = "utf-8") as f:
                for line in f:
                    if "START" in line:
                        words = line.split()
                        keyword = words[1]
                        self.process.start(keyword)
                        print(f"{keyword} added to queue")

                    elif "CALL" in line:
                        words = line.split()
                        self.process.call(words[1], words[2])

                    elif "RETURN" in line:
                        self.process.return_function()

                    elif "RAISE" in line:
                        self.process.raise_exception()

                    else:
                        print(f"invalid command: {line.strip()}")

        except FileNotFoundError:
            print(f"file '{self.file_name}' not found.")