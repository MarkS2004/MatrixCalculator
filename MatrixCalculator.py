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
        
################################################################
# Variables, Constants                                         #
################################################################
MAX_SIZE_OF_Matrix = 10

storedMatrices = {"emptyMatrix": MatrixClass(3,3)}

################################################################
# Functions                                                    #
################################################################
        
#========================MenuFunctions=========================#
        
#------------------------WelcomeMenu---------------------------#
def menu_welcome():
    """brief: this function prints a welcoming message,
    it ends if Enter is pressed"""

    os.system("cls") # clears screen
    print(
"""Der folgende Matrizenrechener wurde von Marvin Wolff, Mark Schaab und Kemal Bagci
im Rahmen der Informatikklausur am 21.03.2024 ertsellt.
Der Rechner kann verschiedene Rechenoperationen durchführen.
Diese werden im folgenden Hauptmenü zur Auswahl bereit gestellt.

Drücke Enter um ins Hauptmenü zu gelangen""")
    
    input(">")

#--------------------VariableManagerMenu-----------------------#
def submenu_variable_manager():
    """brief: this functions prints the VariableManager and lets one navigate,
    it ends if "0" is pressed"""

    while True:
        os.system("cls") # clears screen
        print(
"""Variablenmanager
-----------------------------------------------------
(1) Matrix eingeben
(2) Matrix anzeigen
(3) Matrix löschen
(4) Name ändern
(5) Werte ändern

(0) Zurück zum Hauptmenü

Wähle eine Zahl:""")
        
        match input(">").strip(): # selction of the differnt Choices to change the matrices 
            case "1": input_matrix()
            case "2": show_matrix()
            case "3": delete_matrix()
            case "4": change_matrix_name()
            case "5": change_matrix_value()
            case "0": return
            case _: pass

#--------------------OperationManagerMenu----------------------#
def submenu_operation_manager():
    """brief: this functions prints the OperationsManager and lets one navigate,
    it ends if "0" is pressed"""

    while True:
        os.system("cls") # clears screen
        print(
""" Variablenmanager
-----------------------------------------------------
(1) Matrizen addieren
(2) Matrizen subtrahieren
(3) Matirzen multiplizieren

(0) Zurück zum Hauptmenü

Wähle eine Zahl:""")
        
        match input(">").strip(): # selction of operations 
            case "1": add_matrix()
            case "2": sub_matrix()
            case "3": mul_matrix()
            case "0": return
            case _: pass

#===============FunctionsForVariableManagment==================#

#---------------------InputExistingMatrix----------------------#
def input_existing_matrix():
    """brief: this functions inputs matrix name,
    checks if matrix exists,
    returns valid matrix name"""

    while True:
        name = input(">").strip()

        if str(storedMatrices.get(name)) != "None": # checks if matrix exists
            print("\n!!! Die Matrix existiert bereits !!!")
            print("\nBite gebe einen anderen Namen ein:")
        else: return name # return valid matrix name

#--------------------InputNotExistingMatrix--------------------#
def input_not_existing_matrix():
    """brief: this functions inputs matrix name,
    checks if matrix does not exist,
    returns valid matrix name"""

    while True:
        name = input(">").strip()

        if str(storedMatrices.get(name)) == "None": # checks if matrix does not exist
            print("\n!!! Die Matrix existiert nicht !!!")
            print("\nBite gebe einen anderen Namen ein:")
        else: return name # return valid matrix name

#-----------------------InputMatrixRows------------------------#
def input_matrix_rows():
    """brief: this function takes user input for rows,
    returns valid number of rows"""

    while True:
        rows = input(">").strip()
        try:
            rows = int(rows) # try to convert to int
        except ValueError:
            print("\n!!! Die Anzahl an Zeilen muss eine Ganzzahl sein !!!")
        else:
            if rows < 1 or rows > MAX_SIZE_OF_Matrix: #checks if Matrix is to big
                print(f"\n!!! Die Anzahl an Zeilen muss zwischen 1 und {MAX_SIZE_OF_Matrix} liegen !!!")

            else: return rows
                
        print("\nBitte gebe die Anzahl an gewünschten Zeilen erneut ein:")

#---------------------InputMatrixColumns-----------------------#
def input_matrix_column():
    """brief: this function takes user input for columns,
    returns valid number of columns"""

    while True:
        columns = input(">").strip()
        try:
            columns = int(columns) # try to convert to int
        except ValueError:
            print("\n!!! Die Anzahl an Spalten muss eine Ganzzahl sein !!!")
        else:
            if columns < 1 or columns > MAX_SIZE_OF_Matrix: #checks if Matrix is to big
                print(f"\n!!! Die Anzahl an Zeilen muss zwischen 1 und {MAX_SIZE_OF_Matrix} liegen !!!")

            else: return columns
                
        print("\nBitte gebe die Anzahl an gewünschten Zeilen erneut ein:")

#------------------------InputMatrix---------------------------#
def input_matrix():
    """brief: this fuction lets the user create 
    a new matrix variable"""

    while True:
        os.system("cls") # clears screen
        print("Wie soll die Matrix heißen?")
        name = input_existing_matrix()

        os.system("cls") # clears screen
        print("Wie viele Zeilen soll die Matrix haben?")
        rows = input_matrix_rows()

        os.system("cls") # clears screen
        print("Wie viele Spalten soll die Matrix haben?")
        columns = input_matrix_column()

        # create and store Matrix
        storedMatrices[name] = MatrixClass(rows, columns)

        # Input Values
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                while True:
                    os.system("cls")

                    print(f"{name} =\n {storedMatrices.get(name)}") # prints unfinished matrix

                    value = input(f"Welchen Wert soll das Element an Stelle {i}, {j} haben?\n>").strip()
                    
                    try:
                        value = float(value) # try to convert to float
                    except ValueError:
                        print("\n!!! Bitte gebe eine Ganz- oder Gleitkommazahl ein !!!")
                        input("\nDrücke Enter um erneut einen Wert einzugeben\n>")
                    else:
                        break # goes to next element
                

                storedMatrices.get(name).set_value(i ,j ,value) # sets Value at Element i, j

        # Show Result
        os.system("cls")
        print("Folgende Matrix wurde angelegt:")
        print(f"{name} =\n {storedMatrices.get(name)}")

        # Try Again
        print("\nMöchtes du eine weitere Matrix anlegen?(Y/N)") 
        if input(">") == "Y": pass # repeats input_matrix if Y
        else: return # return to menu

#--------------------ChangeMatrixName--------------------------#
def change_matrix_name():
    """brief: this function lets the user change the name of a matrix"""
    
    os.system("cls") # clears screen
    print_created_matrices()

    print("Wie heißt die Matrix, bei der der Name geändert werden soll?")
    choice = input_not_existing_matrix()
    
    name = input("Was ist der neue Name der Matrix?\n>").strip() 
    storedMatrices[name] = storedMatrices.pop(choice)

#-------------------------showMatrix---------------------------#
def show_matrix():
    """brief: this function lets the user see the value of a matrix"""

    while True:
        os.system("cls") # clears screen
        print_created_matrices()

        print("\nWelche Matrix möchtest du anzeigen?")
        choice = input_not_existing_matrix()
        print(f"{choice} =\n {storedMatrices.get(choice)}")

        print("\nMöchtes du eine weitere Matrix anzeigen?(Y/N)") 
        if input() == "Y": pass # repeats show_matrix if Y
        else: return # return to menu

#----------------------printCreatedMatrices--------------------#
def print_created_matrices():
    """brief: this fuctions prints a list of all created functions"""

    print("Folgende Matrizen wurden angelegt:")
    for i in storedMatrices.keys(): print(f"- {i}") # prints a list of all matrices

#-------------------------deleteMatrix-------------------------#
def delete_matrix():
    """brief: this function lets the user delet a matrix"""

    while True:
        os.system("cls") # clears screen
        print_created_matrices()

        print("\nWelche Matrix möchtest du löschen?")
        choice = input_not_existing_matrix()

        del storedMatrices[choice] # delets the selected matrix

        os.system("cls") # clears screen
        print(f"Die Matrix:{choice} wurde erfolgreich gelöscht\n")

        print("\nMöchtes du eine weitere Matrix löschen?(Y/N)") 
        if input() == "Y": pass # repeats delete_matrix if Y
        else: return # return to menu

#------------------------ChangeMatrixValue---------------------#
def change_matrix_value():
    """brief: this fuction lets the user change a given value"""

    os.system("cls") # clears screen
    print_created_matrices()

    print("\nBei welcher Martix soll der Wert geändert werden?")
    choice = input_not_existing_matrix()

    os.system("cls") # clears screen
    print(f"{choice} =\n {storedMatrices.get(choice)}") # prints the selected matrix
    
    tempMat = storedMatrices.get(choice) # temporary matrix is created
    
    row = int(input("\nIn welcher Zeile der Martix soll der Wert geändert werden?\n")) # user input matrix row

    if row < 1 or row > tempMat.get_rows(): # if row is lower than 1 or select row is larger than given row
        print("Die Matrix besitzt nicht so viele Zeilen") 
        input()
        return
    
    column = int(input("In welcher Spalte der Martix soll der Wert geändert werden?\n")) # user input matrix column
    if column < 1 or column > tempMat.get_columns(): # if column is lower than 1 or select column is larger than given column
        print("Die Matrix besitzt nicht so viele Spalten")
        input()
        return
    
    value = float(input("Gebe den zu ändernden Wert ein:\n")) # user input matrix value
    
    storedMatrices.get(choice).set_value(row,column,value) # library matrix is overwritten with the new value















#=========================addMatrix============================#
def add_matrix():
    os.system("cls")
    while True:
        summand1 = input("Wie heißt der erste Summand?: \n") # input user: name of summand
        if str(storedMatrices.get(summand1)) == "None":   # check if matrix is in dictonary
            print("Die Matrix existiert nicht!")

        summand2 = input("Wie heißt der zweite Summand?: \n") # input user: name of summand
        if str(storedMatrices.get(summand2)) == "None":   # check if matrix is in dictonary
            print("Die Matrix existiert nicht!")
            
        sum = storedMatrices.pop(summand1) + storedMatrices.pop(summand2)
        print(sum)




        print("Press Enter to get back!")
        input()
        break
    
#=========================subMatrix============================#
def sub_matrix():
    os.system("cls")
    while True:
        minuend = input("Wie heißt der Minuend?: \n") # input user: name of minuend
        if str(storedMatrices.get(minuend)) == "None":   # check if matrix is in dictonary
            print("Die Matrix existiert nicht!")

        subtrahend = input("Wie heißt der Subtrahend?: \n") # input user: name of subtrahend
        if str(storedMatrices.get(subtrahend)) == "None":   # check if matrix is in dictonary
            print("Die Matrix existiert nicht!")
           
        difference = storedMatrices.pop(minuend) - storedMatrices.pop(subtrahend)
        print(difference)

        print("Press Enter to get back!")
        input()
        break

#=========================mulMatrix============================#
def mul_matrix():
    os.system("cls")
    while True:
        factor1 = input("Wie heißt der erste Faktor?: \n") # input user: name of summand
        if str(storedMatrices.get(factor1)) == "None":   # check if matrix is in dictonary
            print("Die Matrix existiert nicht!")

        factor2 = input("Wie heißt der zweite Faktor?: \n") # input user: name of summand
        if str(storedMatrices.get(factor2)) == "None":   # check if matrix is in dictonary
            print("Die Matrix existiert nicht!")
            
        product = storedMatrices.pop(factor1) + storedMatrices.pop(factor2)
        print(product)

        print("Press Enter to get back!")
        input()
        break

################################################################
# Main Programm/Menu                                           #
################################################################

menu_welcome()

while True:
    os.system("cls") # clears screen

    print(
"""Hauptmenü
-----------------------------------------------------
(1) Variablenmanager (anlegen, anzeigen, löschen ...)
(2) Mathematische Grundoperationen (+,-,*)
(3) Matrix transponieren
(4) Determinate berechnen

(0) Programm schließen

Wähle eine Zahl:""")

    match input(">").strip():
        case "1": submenu_variable_manager() 
        case "2": submenu_operation_manager()
        case "3": pass
        case "4": pass
        case "0": break
        case _: pass