"""
Author: Preston Dahl 
Date: 2026-10-25
Lab: lab06
Last modified: 2026-10-25
Purpose: Main function that gets all information necessary to start the all devouring blob and prints the final output.
"""

from the_blob import blob

class start:
    def __init__(self):
        self.user_file = input("Enter your desired filename: ")
        self.blob_instance = None
        self.main_file_list = []
        self.main_file_list2 = []
        self.main_file_list3 = []
        self.blob_file_list = []
        self.blob_file_list2 = []
        self.blob_file_list3 = []
        self.pure_character_spaced_list = []
        self.pure_character_spaced_list2 = []
        self.pure_character_spaced_list3 = []
    #Main function that gathers all blob information
    def main(self):
        while True:
            try:
                self.file = open(self.user_file, mode = "r", encoding = "UTF-8")
                for row in self.file:
                    row1 = row.upper()
                    self.main_file_list.append(row1.split())
                self.file2 = open(self.user_file, mode = "r", encoding = "UTF-8")
                for row2 in self.file2:
                    row3 = row2.upper()
                    self.main_file_list2.append(row3.split())
                self.file3 = open(self.user_file, mode = "r", encoding = "UTF-8")
                for row4 in self.file3:
                    row5 = row4.upper()
                    self.main_file_list3.append(row5.split())
                num_rows = int(self.main_file_list[0][0])
                num_cols = int(self.main_file_list[0][1])
                start_row = int(self.main_file_list[1][0])
                start_col = int(self.main_file_list[1][1])
                self.blob_file_list = self.main_file_list[2:]
                self.blob_file_list2 = self.main_file_list2[2:]
                self.blob_file_list3 = self.main_file_list3[2:]

                for line in self.blob_file_list:
                    for string in line:
                        string = list(string)
                        self.pure_character_spaced_list.append(string)
                for line2 in self.blob_file_list2:
                    for string2 in line2:
                        string2 = list(string2)
                        self.pure_character_spaced_list2.append(string2)
                for line3 in self.blob_file_list3:
                    for string3 in line3:
                        string3 = list(string3)
                        self.pure_character_spaced_list3.append(string3)
            #Error catch
                if num_rows<1 or num_cols<1:
                    raise IndexError("Bounds cannot be less than 1")

                if  start_row<0 or start_row>=num_rows or start_col>=num_cols or start_col<0:
                    raise IndexError("Starting positions are out of bounds")
                
                break

            except FileNotFoundError:
                raise FileNotFoundError("File not found")
            
        self.blob_instance = blob(self.pure_character_spaced_list, start_row, start_col, num_rows, num_cols, self.pure_character_spaced_list2, self.pure_character_spaced_list3)
        self.blob_instance.is_valid(start_row, start_col)
        self.blob_instance.blob_path(start_row, start_col)
        for rows in self.blob_instance.blob_map:
            print(*rows)
        print(f"Total eaten: {self.blob_instance.people_eaten}\n")

if __name__== "__main__":
    start().main()

    