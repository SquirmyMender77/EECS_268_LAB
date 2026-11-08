from executive import Executive

class Main():
    def __init__(self):
        self.exec = Executive()
        self.correct_menu_input = ["1", "2", "3"]
        self.user_menu = input(f"Pick a menu option\n1)Add\n2)Print\n3)Exit\nEnter your choice here: ")


    def digit_check(self, values):
        for value in values.split(","):
            if not value.isdigit() or not value.isascii():
                return False

        return True            
    
    def main(self):
        while True:
            if self.user_menu not in self.correct_menu_input:
                print("Invalid menu option. Please try again.")
                self.user_menu=input(f"Pick a menu option\n1)Add\n2)Print\n3)Exit\nEnter your choice here: ")

            if self.user_menu == self.correct_menu_input[0]:
                values = input("Enter a comma-separated list of values to add to the tree: ")

                while not self.digit_check(values) or len(values.split(",")) < 2:
                    values = input("Invalid input. Please enter comma-separated integers: ")

                else:
                    values = values.split(",")
                    self.exec.add_values(values)

            if self.user_menu == self.correct_menu_input[1]:
                display_option = input("Enter traversal option (pre, in, post): ")
                self.exec.bst.visit_option(display_option)

            if self.user_menu == self.correct_menu_input[2]:
                print("Exiting the program...")
                exit()

            print("===============================")
            self.user_menu=input(f"Pick a menu option\n1)Add\n2)Print\n3)Exit\nEnter your choice here: ")

if __name__ == "__main__":
    Main().main()
