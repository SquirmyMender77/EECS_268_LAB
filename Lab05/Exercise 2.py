"""
Author: Preston Dahl
Date: 2026-10-09
Lab: lab05
Last modified: 2026-10-09
Purpose: Uses the first three days to start a recursive calculation for 
         the outbreak where every day after the third is the sum of the previous three days.
"""

def main(day):
    if day <= 3:
        if day == 0:
            print("Invalid day")

        if day == 1:
            sick = 6
            return sick

        if day == 2:
            sick = 20
            return sick

        if day == 3:
            sick = 75
            return sick
        
    if day > 3:
        sick = main(day-3) + main(day-2) + main(day-1)
        return sick
    
    if day < 0:
        print("Invalid day")

print("OUTBREAK!")    
day = int(input("What day do you want a sick count for?: "))
if day == 0:
    sick = main(day)
elif day > 0:
    sick = main(day)
    print(f"Total people with flu: {sick}")