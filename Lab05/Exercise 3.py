"""
Author: Preston Dahl and gemini help on main "-v" mode
Date: 2026-10-09
Lab: lab05
Last modified: 2026-10-09
Purpose: Implements a function to verify if a given number is in the Fibonacci sequence or not 
         and given an index, can calculate the Fibonacci number at that index.
"""

def main(mode, integer):
    if integer == 0:
        return 0

    if integer == 1:
        return 1

    if mode == "-i" and integer > 1:
        return main(mode, integer - 1) + main(mode, integer - 2)
        
    if mode == "-v":
        n = 0
        while True:
            fib = main("-i", n)
            if fib == integer:
                return True
            if fib > integer:
                return False
            n += 1

user = input("Enter mode and value: ").split(" ")

if (len(user) < 2):
    print("Invalid input")

elif not (user[1].isdigit()):
    print("Invalid input")

elif (user[0].lower() != "-i" and user[0].lower() != "-v"):
    print("Invalid input")

elif (int(user[1]) < 0):
    print("Invalid input")

else:
    fibo = main(user[0].lower(), int(user[1]))

    if user[0].lower() == "-i":
        print(fibo)

    elif user[0].lower() == "-v":
        if fibo:
            print(f"{user[1]} is in the sequence")
        else:
            print(f"{user[1]} is not in the sequence")