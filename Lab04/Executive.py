"""
Author: Preston Dahl
Date: 2026-09-30
Lab: lab04
Last modified: 2026-09-30
Purpose: reads commands from the input file and passes execution steps to Browser.
"""
from Browser import Browser

class Executive:
    def __init__(self):
        self.browse = Browser()
    def main(self):
        user_file = input("enter a file name: ")
        with open(user_file, mode='r',encoding='UTF-8') as f:
            for line in f:
                parts = line.split()

                operation = parts[0].lower()

                if operation == "navigate":
                    entry = parts[1]
                    self.browse.navigate(entry)

                elif operation == "back":
                    self.browse.back()

                elif operation == "forward":
                    self.browse.forward()

                elif operation == "history":
                    self.browse.history()

                else:
                    print("invalid operation")

if __name__ == "__main__":
    Executive().main()