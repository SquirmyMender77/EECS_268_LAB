"""
Author: Preston Dahl 
Date: 2026-10-25
Lab: lab06
Last modified: 2026-10-25
Purpose: Implements a all devouring blob with movement that is limited by buildings and spaces it has already been using recursion.
"""

class blob:
    def __init__(self, userfile1, start_row, start_col, num_rows, num_cols, userfile2, userfile3):
        self.start_col = start_col
        self.start_row = start_row
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.reg_map = userfile1
        self.blob_map = userfile2
        self.visited_map = userfile3
        self.people_eaten = 0
        self.sewer_coords = []
        #Gets coordinates of where all @'s are
        for rows in range(self.num_rows):
            for cols in range(self.num_cols):
                if self.reg_map[rows][cols] == "@":
                    self.sewer_coords.append((rows, cols))

    #Validity function that determines where the blob can move
    def is_valid(self, row, col):
        if row <= self.num_rows-1 and row >= 0 and col <= self.num_cols-1 and col >= 0 and self.reg_map[row][col] != "#" and self.visited_map[row][col] != "X":
            return True

        if row <= self.num_rows-1 and row >= 0 and col <= self.num_cols-1 and col >= 0 and self.reg_map[row][col] != "#" and self.visited_map[row][col] != "X":
            return True
                            
        if row <= self.num_rows-1 and row >= 0 and col <= self.num_cols-1 and col >= 0 and self.reg_map[row][col] != "#" and self.visited_map[row][col] != "X":
            return True
                            
        if row <= self.num_rows-1 and row >= 0 and col <= self.num_cols-1 and col >= 0 and self.reg_map[row][col] != "#" and self.visited_map[row][col] != "X":
            return True

        else:
            return False
    #Actual movement of the blob using recursion
    def blob_path(self, row, col):
        self.is_valid(row, col)
        if self.reg_map[row][col] == "P":
            self.blob_map[row][col] = "B"
            self.visited_map[row][col] = "X"
            self.people_eaten += 1
            if self.is_valid(row-1, col):
                self.blob_path(row-1, col)

            if self.is_valid(row, col+1):
                self.blob_path(row, col+1)

            if self.is_valid(row+1, col):
                self.blob_path(row+1, col)

            if self.is_valid(row, col-1):
                self.blob_path(row, col-1)

        if self.reg_map[row][col] == "S":
            self.blob_map[row][col] = "B"
            self.visited_map[row][col] = "X"
            if self.is_valid(row-1, col):
                self.blob_path(row-1, col)

            if self.is_valid(row, col+1):
                self.blob_path(row, col+1)

            if self.is_valid(row+1, col):
                self.blob_path(row+1, col)

            if self.is_valid(row, col-1):
                self.blob_path(row, col-1)
                
        if self.reg_map[row][col] == "@":
            self.visited_map[row][col] = "X"
            if self.is_valid(row-1, col):
                self.blob_path(row-1, col)

            if self.is_valid(row, col+1):
                self.blob_path(row, col+1)

            if self.is_valid(row+1, col):
                self.blob_path(row+1, col)

            if self.is_valid(row, col-1):
                self.blob_path(row, col-1)

            for i, j in self.sewer_coords:
                if self.visited_map[i][j] != "X":
                    self.visited_map[i][j] = "X"
                    self.blob_path(i, j)
