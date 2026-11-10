from executive import executive

class Main:
    def __init__(self):
        self.exec = executive()
        self.OG_file = []
        self.American_names = []
        self.pokedex_IDs = []
        self.japanese_names = []
        self.menu_options = ["1", "2", "3", "4", "5", "6"]
        self.user_file = input("Enter a File Name: ")


    def main(self):
        while True:
            try:
                with open(self.user_file, mode = "r", encoding = "UTF-8") as f:
                    for line in f:
                        line = line.lower()
                        line = line.split()
                        self.OG_file.append(line)

                for row in self.OG_file: 
                    if len(row) < 3:
                        self.user_file = input("File is not formatted correctly, please try again: ")
                        self.main()

                    else:
                        self.American_names.append(row[0])
                        self.pokedex_IDs.append(row[1])
                        self.japanese_names.append(row[2])

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
                        self.exec.Add(self.American_names, self.pokedex_IDs, self.japanese_names)

                    if user_input == self.menu_options[1]:
                        self.exec.search(self.OG_file, self.pokedex_IDs, self.American_names, self.japanese_names)

                    if user_input == self.menu_options[2]:
                        self.exec.print()

                    if user_input == self.menu_options[3]:
                        self.exec.remove()

                    if user_input == self.menu_options[4]:
                        try:
                            if self.exec.bst_copy.instance_created ==  True:                               
                                print("A copy cannot be created because one is already active.")

                        except AttributeError:
                            self.exec.copy(self.OG_file)

                    if user_input == self.menu_options[5]:
                        exit()

            except FileNotFoundError:
                user_file = input("File not found, please try again: ")

if __name__ == "__main__":
    Main().main()
