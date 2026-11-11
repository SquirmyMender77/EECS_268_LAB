from pokedex_funcs import pokedex_funcs
from pokemon import Pokemon

class Pokedex:
    def __init__(self):
        self.poke_funcs = pokedex_funcs()
        self.OG_file = []
        self.American_names = []
        self.pokedex_IDs = []
        self.japanese_names = []
        self.menu_options = ["1", "2", "3", "4", "5", "6"]
        self.user_file = input("Enter a File Name: ")


    def pokedex_menu(self):
        try:
            with open(self.user_file, mode = "r", encoding = "UTF-8") as f:
                for line in f:
                    line = line.lower()
                    line = line.split()
                    self.OG_file.append(line)
                    self.poke = Pokemon(line[0], int(line[1]), line[2])
                    self.poke_funcs.pokedex_internals.add(self.poke)

            
            for row in self.OG_file: 
                if len(row) < 3:
                    self.user_file = input("File is not formatted correctly, please try again: ")
                    self.pokedex_menu()
            
                else:
                    self.American_names.append(row[0])
                    self.pokedex_IDs.append(row[1])
                    self.japanese_names.append(row[2])

        except FileNotFoundError:
            self.user_file = input("File not found, please try again: ")
            self.pokedex_menu()

        while True:
            print(f"HUMAN VERIFIED\n"
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                "Welcome to the Pokedex!\n"
                "1) ADD Pokemon Entry\n"
                "2) Search for a specific Pokemon\n"
                "3) List Apprehended Pokemon\n"
                "4) Remove Pokemon Entry\n"
                "5) Copy Apprehended Pokemon List\n"
                "6) Exit Pokedex")
            user_input = input("Enter a choice from above: ")
            while user_input not in self.menu_options:
                user_input = input("Invalid option, please try again: ")
                
            if len(self.American_names) > 0 and len(self.pokedex_IDs) > 0 and len(self.japanese_names) > 0:
                if user_input == self.menu_options[0]:
                    self.poke_funcs.Add(self.OG_file)

                if user_input == self.menu_options[1]:
                    self.poke_funcs.search()

                if user_input == self.menu_options[2]:
                    self.poke_funcs.print()

                if user_input == self.menu_options[3]:
                    self.poke_funcs.remove()

                if user_input == self.menu_options[4]:
                    try:
                        if self.poke_funcs.pokedex_internals_copy.instance_created ==  True:                               
                            print("A copy cannot be created because one already exists.")

                    except AttributeError:
                        self.poke_funcs.copy(self.OG_file)

                if user_input == self.menu_options[5]:
                    exit()

if __name__ == "__main__":
    Pokedex().pokedex_menu()
