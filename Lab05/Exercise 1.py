"""
Author: Preston Dahl 
Date: 2026-10-09
Lab: lab05
Last modified: 2026-10-09
Purpose: Implements a function to calculate the power of a number using recursion.
"""

try:
    base = float(input("enter the base: "))
    power = float(input("enter the exponent: "))
    def raise_power(base, power):

        if power == 0:
            return 1
                      
        if power < 0:
            print("the power cannot be negative. enter a positive number")
        return base * raise_power(base, power-1)
    print(raise_power(base, power))
except ValueError:
    print("input has to be a number")
