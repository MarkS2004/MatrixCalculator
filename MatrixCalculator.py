################################################################
#            ___  ___      _   _____       _                   #
#            |  \/  |     | | /  __ \     | |                  #
#            | .  . | __ _| |_| /  \/ __ _| | ___              #
#            | |\/| |/ _` | __| |    / _` | |/ __|             #
#            | |  | | (_| | |_| \__/\ (_| | | (__              #
#            \_|  |_/\__,_|\__|\____/\__,_|_|\___|             #
################################################################
# file name: MatrixCalculator.py                               #
# date: 05.03.2023                                             #
# authors: Marvin Wolff, Kemal Bagci, Mark Schaab              #
# brief: This Programm can do various matrix calculations      #
################################################################

################################################################
# Modules                                                      #
################################################################
import os

################################################################
# Variables, Constants                                         #
################################################################
MAX_SIZE_OF_Matrix = 10

storedMatrices = dict()

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

        if self._rows == other._rows and self._columns == other._columns: # checks if matrices are the same size

            result = MatrixClass(self._rows, self._columns)

            for i in range (self._rows): # goes through the rows of the matrices  
                for j in range (self._columns): # goes through the columns of the matrices
                    result._matrix[i][j] = self._matrix[i][j] + other._matrix[i][j] # adds the matrices

            return result

        else:
            raise ValueError("The Matrices are not the same size! They can not be added!") # ValueError message

#=========================SubMethod============================#
    def __sub__(self, other):
        
        if self._rows == other._rows and self._columns == other._columns: # checks if matrices are the same size

            result = MatrixClass(self._rows, self._columns)

            for i in range (self._rows): # goes through the rows of the matrices  
                for j in range (self._columns): # goes through the columns of the matrices
                    result._matrix[i][j] = self._matrix[i][j] - other._matrix[i][j] # substracts the matrices

            return result
                
        else:
            raise ValueError("The Matrices are not the same size! They can not be subtracted!") # ValueErrror message

#==========================MulMethod===========================#
    def __mul__(self, other):

        if self._rows == other._columns and self._columns == other._rows:
             
            result = MatrixClass(self._rows, other._columns) # initialize result matrix

            for i in range (self._rows): # goes through the rows of the matrices 
                for j in range (other._columns): # goes through the columns of the matrices
                    for k in range (self._columns): # goes through the columns of the matrices
                        result._matrix[i][j] += (self._matrix[i][k] * other._matrix[k][j]) # multiplicates the matrices
                    
            return result
                
        else:
            raise ValueError("The Matrices are not the same size! They can not be mutiplicated!") # ValueErrror message

#==========================EqMethod============================#
    def __eq__(self, other):
        if self._rows != other._rows and self._columns != other._columns: # checks if matrices are not the same size
            return False
        
        for i in range(self._rows): # goes through the rows of the Matrices  
            for j in range(self._columns): # goes through the columns of the Matrices
                if self._matrix[i][j] != other._matrix[i][j]: # checks if the different elements in the matrices are not the same  
                    return False
        
        return True # if everthing is identical, "True" will be returned 

################################################################
# Functions                                                    #
################################################################

#========================InputMatrix===========================#
def input_matrix():
    pass

#=====================changeMatrixName=========================#
def change_matrix_name():
    choice = input("Wie heißt die Matrix, bei welcher der Name geändert werden soll?: \n") # input user: name of matrix, which should be changed
    if str(storedMatrices.get(choice)) == "None":   # check if matrix is in dictonary
        print("Die Matrix existiert nicht!")
        input()
        return  # leave if matrix is not in dictonary
    
    name = input("Was ist der neue Name der Matrix?: \n")    # new name of Matrix 
    storedMatrices[name] = storedMatrices.pop(choice)

#=========================showMatrix===========================#
def show_matrix():
    while True:
        os.system("cls") # clears screen

        print("Folgende Matrizen wurden angelegt:")
        for i in storedMatrices.keys(): print(f"- {i}") # prints a list of all matrix keys

        choice = input("\nWelche Matrix möchtest du anzeigen?\n").strip()

        if str(storedMatrices.get(choice)) != "None": # checks if matrix exists
            print(f"{choice} =\n {storedMatrices.get(choice)}") # prints the matrix

        else:
            print("Die eingegebene Matrix existiert nicht")

        print("\nMöchtes du eine weitere Matrix anzeigen?(Y/N)") 
        if input() == "Y": pass # repeats show_matrix if Y
        else: return # return to menu

#===================changeMatrixValue===========================#
def change_matrix_value():
    pass

#=======================deleteMatrix===========================#
def delete_matrix():
    pass

################################################################
# Main Programm                                                #
################################################################
A = MatrixClass(3, 3)

for i in range(A.get_rows()):
    for j in range(A.get_columns()):
        A.set_value(i+1, j+1, i*A.get_rows() + j)

B = MatrixClass(3, 3)

for i in range(B.get_rows()):
    for j in range(B.get_columns()):
        B.set_value(i+1, j+1, i*B.get_rows() + j - 18)


storedMatrices["matA"] = A

storedMatrices["matB"] = B

show_matrix()
#=========================SubCaption===========================#
