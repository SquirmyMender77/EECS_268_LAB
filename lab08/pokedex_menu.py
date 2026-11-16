"""
Author: Preston Dahl 
Date: 2026-11-16
Lab: lab08
Last modified: 2026-11-16
Purpose: Main Pokedex Class that implements a pokedex_manu, handles a file input, and starts the pokedex_funcs Class
"""

from pokedex_funcs import pokedex_funcs
from pokemon import Pokemon

class Pokedex:
    def __init__(self):
        self.poke_funcs = pokedex_funcs()
        self.OG_file = []
        self.American_names = []
        self.pokedex_IDs = []
        self.japanese_names = []
        #for validity
        self.menu_options = ["1", "2", "3", "4", "5", "6"]
        self.user_file = input("Enter a File Name: ")


    def pokedex_menu(self):
        try:
            with open(self.user_file, mode = "r", encoding = "UTF-8") as f:
                for line in f:
                    line = line.lower()
                    line = line.split()
                    self.OG_file.append(line)
            
            for row in self.OG_file:
                #Adding each part to a different list to then check if the entry exists in the for loop below
                self.American_names.append(row[0])
                self.pokedex_IDs.append(row[1])
                self.japanese_names.append(row[2])
                self.poke = Pokemon(row[0], int(row[1]), row[2])
                self.poke_funcs.pokedex_internals.add(self.poke)
            
            for index in range(len(self.American_names)): 
                if len(self.American_names[index]) == "" and len(self.pokedex_IDs[index]) == "" and len(self.japanese_names[index]) == "":
                    self.user_file = input("File Entry is Empty, please try again: ")
                    self.pokedex_menu()
            
            else:
                print(f" {"".center(146, "_")}")                     
                print(f"|{"HUMAN VERIFIED".center(146)}|")
                print(f"|{"Welcome to the Pokedex!".center(146)}|")

        except FileNotFoundError:
            self.user_file = input("File not found, please try again: ")
            self.pokedex_menu()

        while True:
            #User menu
            print(f"|{"".center(146, "~")}|")                     
            print(f"|{"1) ADD Pokemon Entry".center(146)}|")
            print(f"|{"2) Search for a specific Pokemon".center(146)}|")
            print(f"|{"3) List Apprehended Pokemon".center(146)}|")
            print(f"|{"4) Remove Pokemon Entry".center(146)}|")
            print(f"|{"5) Copy Apprehended Pokemon List".center(146)}|")
            print(f"|{"6) Exit Pokedex".center(146)}|")
            print(f"|{"".center(146, "~")}|")

            prompt = "Enter a choice from above: "
            centered = prompt.center(146)
            clean = centered[:146 // 2 + len(prompt) // 2]
            user_input = input(f"|{clean}")
            
            while user_input not in self.menu_options:
                prompt = "Invalid option, please try again: "
                centered = prompt.center(146)
                clean = centered[:146 // 2 + len(prompt) // 2]
                user_input = input(f"|{clean}")

            print(f"|{"".center(146)}|")
                
            if user_input == self.menu_options[0]:
                self.poke_funcs.Add()

            if user_input == self.menu_options[1]:
                self.poke_funcs.search()

            if user_input == self.menu_options[2]:
                self.poke_funcs.print()

            if user_input == self.menu_options[3]:
                self.poke_funcs.remove()

            if user_input == self.menu_options[4]:
                try:
                    if self.poke_funcs.pokedex_internals_copy.instance_created ==  True:
                        print(f"|{"A copy cannot be created because one already exists.".center(146)}|")

                except AttributeError:
                    print(f"|{"Creating a copy...".center(146)}|")
                    print(f"|{f"".center(146)}|")
                        
                    self.poke_funcs.copy(self.poke_funcs.pokedex_internals.root)
                        
                    print(f"|{"Copy created successfully.".center(146)}|")

            if user_input == self.menu_options[5]:
                print(f"|{"Exiting...".center(146)}|")
                print(f"|{"".center(146, "_")}|")
                exit()
              
                
if __name__ == "__main__":
    Pokedex().pokedex_menu()
