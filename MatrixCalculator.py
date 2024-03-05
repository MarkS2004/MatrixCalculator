################################################################
# ___  ___      _   _____       _                              #
# |  \/  |     | | /  __ \     | |                             #
# | .  . | __ _| |_| /  \/ __ _| | ___                         #
# | |\/| |/ _` | __| |    / _` | |/ __|                        #
# | |  | | (_| | |_| \__/\ (_| | | (__                         #
# \_|  |_/\__,_|\__|\____/\__,_|_|\___|                        #
################################################################
# file name: MatrixCalculator.py                               #
# date: 05.03.2023                                             #
# authors: Marvin Wolff, Kemal Bagci, Mark Schaab              #
# brief: This Programm can do various matrix calculations      #
################################################################

################################################################
# Variables, Constants                                         #
################################################################

################################################################
# Matrix Class                                                 #
################################################################
class MatrixClass:

#=========================Constructor==========================#
    def __init__(self, rows, columns):
        self._rows, self._columns = rows, columns

        self._matrix = [[0]*self._columns]*self._rows

#==========================Getters=============================#
    def get_value(self, row, column): return self._matrix[row-1][column-1]
    
    def get_columns(self): return self._columns

    def get_rows(self): return self._rows

#==========================Setters=============================#
    def set_value(self, row, column, value):
        pass
#=====================StringRepresentation=====================#
    def __str__(self):
        outputString = "\t┌" + "\t"*(self._columns + 1) + "┐\n" # upper part of matrix

        for i in range(self._rows):
            outputString += "\t│" # left part of matrix

            for j in range(self._columns):
                outputString += f"\t{self._matrix[i][j]}" # field with elements

            outputString += "\t│\n" # right part of matrix

        outputString += "\t└" + "\t"*(self._columns + 1) + "┘"  # lower part of matrix

        return outputString
        
#=========================AddMethode===========================#
    def __add__(self, other):

        if self._rows == other._rows and self._columns == other._columns:       # Checks if matrices are the same size
            for i in range (self._rows):                                        # Goes throw the rows of the matrices  
                for j in range (self._columns):                                 # Goes throw the columns of the matrices
                    self._matrix[i][j] += other._matrix[i][j]                   # added the matrices

                    return self

        else:
            raise ValueError ("The Matrices are not the same size! They can not be added!") # ValueErrror message

    
#=========================SubMethode===========================#
    def __sub__(self, other):
        
         if self._rows == other._rows and self._columns == other._columns:      # Checks if matrices are the same size
            for i in range (self._rows):                                        # Goes throw the rows of the matrices  
                for j in range (self._columns):                                 # Goes throw the columns of the matrices
                    self._matrix[i][j] -= other._matrix[i][j]                   # Substracted the matrices

                    return self
                
         else:
            raise ValueError("The Matrices are not the same size! They can not be subtracted!") # ValueErrror message


#=========================MulMethode===========================#
    def __mul__(self, other):
        pass

#==========================EqMethode===========================#
    def __eq__(self, other):
        pass

################################################################
# Main Programm                                                #
################################################################

A = MatrixClass(10,10)

print(A.get_rows())
#=========================SubCaption===========================#

################################################################
# Functions                                                    #
################################################################