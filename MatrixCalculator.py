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
MAX_SIZE_OF_Matrix = 10

################################################################
# Matrix Class                                                 #
################################################################
class MatrixClass:

#=========================Constructor==========================#
    def __init__(self, rows, columns):
        if not type(rows) is int: # check if rows  are intergers
            raise TypeError("rows must be integers")
        
        if not type (columns) is int: # check if columns are intergers
            raise TypeError("rcolumns must be integers")
        
        if rows < 1 or rows > MAX_SIZE_OF_Matrix: # check if 1 <= rows <= Max size
            raise ValueError(f"rows must be between 1 and {MAX_SIZE_OF_Matrix}")
        
        if columns < 1 or columns > MAX_SIZE_OF_Matrix: # check if 1 <= columns <= Max size
            raise ValueError(f"columns must be between 1 and {MAX_SIZE_OF_Matrix}")
        
        self._rows, self._columns = rows, columns 

        self._matrix = [[0]*self._columns]*self._rows

#==========================Getters=============================#
    def get_value(self, row, column): return self._matrix[row-1][column-1]
    
    def get_columns(self): return self._columns

    def get_rows(self): return self._rows

#==========================Setter==============================#
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
        pass

#=========================SubMethode===========================#
    def __sub__(self, other):
        pass

#=========================MulMethode===========================#
    def __mul__(self, other):
        pass

#==========================EqMethode===========================#
    def __eq__(self, other):
        pass

################################################################
# Main Programm                                                #
################################################################

A = MatrixClass(10, 1)

print(A)
#=========================SubCaption====================f=======#


################################################################
# Functions                                                    #
################################################################