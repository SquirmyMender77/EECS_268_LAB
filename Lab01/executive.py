
class Executive:
    def __init__(self, file_name):
        self.file_name = file_name
    def user_interaction(self):
        while True:
            print("============\n"
            "1. Print all games highest Gibbons rating to lowest\n"
            "2. Edit a game's rating\n"
            "3. Obtain a game's name and year from the user then ask them to enter a new Gibbons rating\n"
            "3. Print all games with a weight equal to or lower than a provided weight\n"
            "4. The People VS Dr. Gibbons\n"
            "5. Print based on player count\n"
            "6. Exit the program\n"
            "============\n")
            user_input = input("Choose an option: ")
            if user_input == "1":
                1 
            if user_input == "6":
                print("Shutting Down...")
                break
        return
    def section_extractor(self):
        board_game_info=[]
        game_ratings=[]
        game_weights=[]
        board_game_name=[]
        with open(self.file_name, 'r') as file:
            for line in file:
                line = line.lower().split()
                board_game_info.append(line)
            for i in range(0,len(board_game_info)):
                print(board_game_info[i])
