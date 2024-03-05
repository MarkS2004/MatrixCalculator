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
        if not type(rows) is int: # check if rows is interger
            raise TypeError("rows must be integers")
        
        if not type (columns) is int: # check if columns is interger
            raise TypeError("columns must be integers")
        
        if rows < 1 or rows > MAX_SIZE_OF_Matrix: # check if 1 <= rows <= max size
            raise ValueError(f"rows must be between 1 and {MAX_SIZE_OF_Matrix}")
        
        if columns < 1 or columns > MAX_SIZE_OF_Matrix: # check if 1 <= columns <= max size
            raise ValueError(f"columns must be between 1 and {MAX_SIZE_OF_Matrix}")
        
        self._rows, self._columns = rows, columns 

        self._matrix = [[0 for i in range(self._columns)] for j in range(self._rows)] # create 2d Array

#==========================Getters=============================#
    def get_value(self, row, column): return self._matrix[row-1][column-1]
    
    def get_columns(self): return self._columns

    def get_rows(self): return self._rows

#==========================Setter==============================#
    def set_value(self, row, column, value):
        if (not type(value) is int) and (not type(value) is float): # check if value is integer or float
            raise TypeError("value must be integer or float")
        
        if (not type(row) is int) or (not type(column) is int): # check if row and column is integer
            raise TypeError("row and column must be integer")
        
        if row < 1 or row > self._rows:
            raise ValueError(f"row must be between 1 and {self._rows}") # check if 1 <= row <= number of rows
                
        if column < 1 or column > self._columns:
            raise ValueError(f"column must be between 1 and {self._columns}") # check if 1 <= column <= number of columns
        
        self._matrix[row-1][column-1] = value

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
        
#=========================AddMethod============================#
    def __add__(self, other):

        if self._rows == other._rows and self._columns == other._columns:       # Checks if matrices are the same size
            for i in range (self._rows):                                        # Goes throw the rows of the matrices  
                for j in range (self._columns):                                 # Goes throw the columns of the matrices
                    self._matrix[i][j] += other._matrix[i][j]                   # added the matrices

                    return self

        else:
            raise ValueError("The Matrices are not the same size! They can not be added!") # ValueError message

    
#=========================SubMethod============================#
    def __sub__(self, other):
        
        if self._rows == other._rows and self._columns == other._columns:       # Checks if matrices are the same size
            for i in range (self._rows):                                        # Goes throw the rows of the matrices  
                for j in range (self._columns):                                 # Goes throw the columns of the matrices
                    self._matrix[i][j] -= other._matrix[i][j]                   # Substracted the matrices

                    return self
                
        else:
            raise ValueError("The Matrices are not the same size! They can not be subtracted!") # ValueErrror message


#==========================MulMethod===========================#
    def __mul__(self, other):

        if self._rows == other._columns and self._columns == other._rows:                               # Checks conditions
             
             result = MatrixClass(self._rows, other._columns)    # Initialize result matrix

             for i in range (self._rows):                                                             # Goes throw the rows of selfmatrix  
                for j in range (other._columns):                                                      # Goes throw the columns of othermatrix
                    for k in range (self._columns):                                                   # Goes throw
                        result._matrix[i][j] += (self._matrix[i][k] * other._matrix[k][j])            # Mutiplicated the matrices
                    
                    return result
                
        else:
            raise ValueError("The Matrices are not the same size! They can not be mutiplicated!") # ValueErrror message

#==========================EqMethod============================#
    def __eq__(self, other):
        if self._rows != other._rows and self._columns != other._columns:       # Checks if matrices are not the same size
            return False
        
        for i in range(self._rows):                                             # Goes throw the rows of the Matrices  
            for j in range(self._columns):                                      # Goes throw the columns of the Matrices
                if self._matrix[i][j] != other._matrix[i][j]:                   # Checks if the differnt variables in the matrices are not the same  
                    return False
        
        return True                                                             # If there erverthing is identical "True" will be returned 
                    
################################################################
# Main Programm                                                #
################################################################
A = MatrixClass(3, 3)

for i in range(A.get_rows()):
    for j in range(A.get_columns()):
        A.set_value(i+1, j+1, i*A.get_rows() + j)

print(f"A =\n{A}")

B = MatrixClass(3, 3)

for i in range(B.get_rows()):
    for j in range(B.get_columns()):
        B.set_value(i+1, j+1, i*B.get_rows() + j)

print(f"B =\n{B}")

#=========================SubCaption====================f=======#


################################################################
# Functions                                                    #
################################################################