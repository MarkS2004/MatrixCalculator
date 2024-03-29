################################################################
# Matrix Class                                                 #
################################################################
# file name: MatrixClass.py                                    #
# date: 19.03.2023                                             #
# authors: Marvin Wolff, Kemal Bagci, Mark Schaab              #
# brief: This program is a MatrixClass for the main program    #
#        The methodes are:                                     #
#        __init__ (initialiser), get_value, get_columns,       #
#        get_rows, set_value, __str__(string rep for print),   #
#        __add__, __sub__, __mul__ (operator overloading),     #
#        transpose                                             #               
################################################################

################################################################
# Config                                                       #
################################################################
MAX_SIZE_OF_Matrix = 10

################################################################
# Matrix Class                                                 #
################################################################
class MatrixClass:
#=========================Constructor==========================#
    def __init__(self, rows, columns):
        """brief: initializes a matrix"""

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
        """brief: sets a value in a matrix"""

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
        """brief: ouput of matrix if represented as string"""

        outputString = "\t┌" + "\t"*(self._columns + 1) + "┐\n" # upper part of matrix-representation

        for i in range(self._rows):
            outputString += "\t│" # left part of matrix-representation

            for j in range(self._columns):
                outputString += f"\t{self._matrix[i][j]}" # field with elements

            outputString += "\t│\n" # right part of matrix-representation

        outputString += "\t└" + "\t"*(self._columns + 1) + "┘"  # lower part of matrix-representation

        return outputString
        
#=========================AddMethod============================#
    def __add__(self, other):
        """brief: adds two matrices"""

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
        """brief: substacts two matrices"""

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
        """brief: multiplies two matrices"""

        if self._rows == other._columns and self._columns == other._rows:
             
            result = MatrixClass(self._rows, other._columns) # initialize result matrix

            for i in range (self._rows): # goes through the rows of the result-matrix
                for j in range (other._columns): # goes through the columns of the result-matrix

                    for k in range (self._columns): # goes through the columns/rows of the matrices
                        result._matrix[i][j] += (self._matrix[i][k] * other._matrix[k][j]) # multiplicates the matrices
                    
            return result
                
        else:
            raise ValueError("The Matrices are not the same size! They can not be mutiplicated!") # ValueErrror message

#======================TransposeMethod=========================#
    def transpose(self):

        tempMat = MatrixClass(self._columns, self._rows) # tempory Matrix with switched dimensions

        for i in range (self._columns): # goes through the rows of the matrix 
            for j in range(self._rows): # goes through the columns of the matrix 
                tempMat._matrix[i][j] = self._matrix[j][i] # switches position
        
        return tempMat
           