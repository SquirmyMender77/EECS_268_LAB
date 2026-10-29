"""
Author: Preston Dahl
KUID: [ID REDACTED]
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Entry point script for running the process simulator program.
"""

from executive import Executive

def main():
    """Ask for an input filename and run
    the executive."""
    file_name = input("Enter file name: ")
    executive = Executive(file_name)
    executive.run()

if __name__ == "__main__":
    main()
    