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
    while True:
        os.system("cls") # clears screen
        name = input_matrix_name()

        os.system("cls") # clears screen
        rows = input_matrix_rows()

        os.system("cls") # clears screen
        columns = input_matrix_column()

        storedMatrices[name] = MatrixClass(rows, columns) # create and store Matrix
        #-----------------------------ValueInput---------------------------#
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                while True:
                    os.system("cls")

                    print(f"{name} =\n {storedMatrices.get(name)}") # prints unfinished matrix

                    value = input(f"Welchen Wert soll das Element an Stelle {i}, {j} haben?\n").strip()
                    
                    try:
                        value = float(value) # try to convert to float
                    except ValueError:
                        print("\n!!! Bitte gebe eine Ganz- oder Gleitkommazahl ein !!!")
                        input("\nDrücke Enter um erneut einen Wert einzugeben")
                    else:
                        break # goes to next element
                

                storedMatrices.get(name).set_value(i ,j ,value) # sets Value at Element i, j

        #-----------------------------showResult---------------------------#
        os.system("cls")
        print("Folgende Matrix wurde angelegt:")
        print(f"{name} =\n {storedMatrices.get(name)}")

        #-----------------------------TryAgain?---------------------------#
        print("\nMöchtes du eine weitere Matrix anlegen?(Y/N)") 
        if input() == "Y": pass # repeats input_matrix if Y
        else: return # return to menu

#=======================inputMatrixName===========================#
def input_matrix_name():
    print("Wie soll die Matrix heißen?")
    while True:
        name = input().strip()

        if str(storedMatrices.get(name)) != "None": # checks if matrix exists
            print("\n!!! Die Matrix existiert bereits !!!")
            print("\nBite gebe einen anderen Namen ein:")
        else: return name # leaves input_matrix_name

#=======================inputMatrixRows===========================#
def input_matrix_rows():
    print("Wie viele Zeilen soll die Matrix haben?")
    while True:
        rows = input().strip()
        try:
            rows = int(rows) # try to convert to int
        except ValueError:
            print("\n!!! Die Anzahl an Zeilen muss eine Ganzzahl sein !!!")
        else:
            if rows < 1 or rows > MAX_SIZE_OF_Matrix: #checks if Matrix is to big
                print(f"\n!!! Die Anzahl an Zeilen muss zwischen 1 und {MAX_SIZE_OF_Matrix} liegen !!!")

            else: return rows # leave input_matrix_rows
                
        print("\nBitte gebe die Anzahl an gewünschten Zeilen erneut ein:")

#=======================inputMatrixColumns===========================#
def input_matrix_column():
    print("Wie viele Spalten soll die Matrix haben?")
    while True:
        columns = input().strip()
        try:
            columns = int(columns) # try to convert to int
        except ValueError:
            print("\n!!! Die Anzahl an Spalten muss eine Ganzzahl sein !!!")
        else:
            if columns < 1 or columns > MAX_SIZE_OF_Matrix: #checks if Matrix is to big
                print(f"\n!!! Die Anzahl an Zeilen muss zwischen 1 und {MAX_SIZE_OF_Matrix} liegen !!!")

            else: return columns # leave input_matrix_column
                
        print("\nBitte gebe die Anzahl an gewünschten Zeilen erneut ein:")

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
            os.system("cls") # clears screen
            print(f"{choice} =\n {storedMatrices.get(choice)}") # prints the matrix

        else:
            print("\n!!! Die eingegebene Matrix existiert nicht !!!")

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

# input_matrix()
input_matrix()
show_matrix()
#=========================SubCaption===========================#
