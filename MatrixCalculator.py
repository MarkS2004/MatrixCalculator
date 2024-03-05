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

#===========================Getter=============================#
    @property
    def matrix(self, row, column):
        pass

#===========================Setter=============================#
    @matrix.setter
    def matrix(self, row, column, value):
        pass

#=====================StringRepresentation=====================#
    def __str__(self):
        pass
        
#=========================AddMethode===========================#
    def __add__(self, other):

        if self._rows == other._rows and self._columns == other._columns:       # Checks if Matrices are the same size
            for i in range (self._rows):                                        # Goes throw the rows of the Matrices  
                for j in range (self._columns):                                 # Goes throw the columns of the Matrices
                    self._matrix[i][j] += other._matrix[i][j] 

                    return self

        else:
            raise ValueError ("The Matrices are not the same size! They can not be added!") # Errror message

    

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

#=========================SubCaption===========================#

################################################################
# Functions                                                    #
################################################################