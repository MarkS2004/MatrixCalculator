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

            for i in range (self._rows): # goes through the rows of the matrices 
                for j in range (other._columns): # goes through the columns of the matrices
                    for k in range (self._columns): # goes through the columns of the matrices
                        result._matrix[i][j] += (self._matrix[i][k] * other._matrix[k][j]) # multiplicates the matrices
                    
            return result
                
        else:
            raise ValueError("The Matrices are not the same size! They can not be mutiplicated!") # ValueErrror message
        
################################################################
# Variables, Constants, Objects                                #
################################################################
MAX_SIZE_OF_Matrix = 10

NAME_EMERG_MAT = "emergMat"
stored_matrices = {NAME_EMERG_MAT: MatrixClass(1,1)} # dictionary
# emergency Matrix for if the user is forced to choose a matrix

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
(1) Matrix anlegen
(2) Matrix anzeigen
(3) Matrix löschen
(4) Namen ändern
(5) Wert ändern

(0) Zurück zum Hauptmenü

Wähle eine Nummer:""")
        
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
"""Operationsmanager
-----------------------------------------------------
(1) Matrizen addieren
(2) Matrizen subtrahieren
(3) Matrizen multiplizieren

(0) Zurück zum Hauptmenü

Wähle eine Nummer:""")
        
        match input(">").strip(): # selction of operations 
            case "1": add_matrix()
            case "2": sub_matrix()
            case "3": mul_matrix()
            case "0": return
            case _: pass


#===============FunctionsForVariableManagment==================#
            
#---------------------InputExistingMatrix----------------------#
def input_not_existing_matrix():
    """brief: this functions inputs matrix name,
    checks if matrix exists,
    returns valid matrix name"""

    while True:
        name = input(">").strip()

        if str(stored_matrices.get(name)) != "None": # checks if matrix exists
            print("\n!!! Die Matrix existiert bereits !!!")
            print("\nBite gebe einen anderen Namen ein:")
        else: return name # return valid matrix name

#--------------------InputNotExistingMatrix--------------------#
def input_existing_matrix():
    """brief: this functions inputs matrix name,
    checks if matrix does not exist,
    returns valid matrix name"""

    while True:
        name = input(">").strip()

        if str(stored_matrices.get(name)) == "None": # checks if matrix does not exist
            print("\n!!! Die Matrix existiert nicht !!!")
            print("\nBite gebe einen anderen Namen ein:")
        else: return name # return valid matrix name

#-----------------------InputMatrixRows------------------------#
def input_matrix_row(max_size):
    """brief: this function takes user input for row,
    returns valid number for row"""

    while True:
        row = input(">").strip()
        try:
            row = int(row) # try to convert to int
        except ValueError:
            print("\n!!! Der Wert für die Zeile(n) muss muss eine Ganzzahl sein !!!")
        else:
            if row < 1 or row > max_size: #checks if Matrix is to big
                print(f"\n!!! Der Wert für die Zeile(n) muss zwischen 1 und {max_size} liegen !!!")

            else: return row
                
        print("\nBitte gebe die Zeile(n) erneut ein:")

#----------------------InputMatrixColumn-----------------------#
def input_matrix_column(max_size):
    """brief: this function takes user input for columns,
    returns valid number of columns"""

    while True:
        column = input(">").strip()
        try:
            column = int(column) # try to convert to int
        except ValueError:
            print("\n!!! Der Wert für die Spalte(n) muss muss eine Ganzzahl sein !!!")
        else:
            if column < 1 or column > max_size: #checks if Matrix is to big
                print(f"\n!!! Der Wert für die Spalte(n) muss zwischen 1 und {max_size} liegen !!!")

            else: return column
                
        print("\nBitte gebe die Spalte(n) erneut ein:")

#------------------------InputMatrix---------------------------#
def input_matrix():
    """brief: this fuction lets the user create 
    a new matrix variable"""

    while True:
        os.system("cls") # clears screen
        print("Wie soll die Matrix heißen?")
        name = input_not_existing_matrix()

        os.system("cls") # clears screen
        print("Wie viele Zeilen soll die Matrix haben?")
        rows = input_matrix_row(MAX_SIZE_OF_Matrix)

        os.system("cls") # clears screen
        print("Wie viele Spalten soll die Matrix haben?")
        columns = input_matrix_column(MAX_SIZE_OF_Matrix)

        # create and store Matrix
        stored_matrices[name] = MatrixClass(rows, columns)

        # Input Values
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                while True:
                    os.system("cls")

                    print(f"{name} =\n {stored_matrices.get(name)}") # prints unfinished matrix

                    value = input(f"Welchen Wert soll das Element an Stelle {i}, {j} haben?\n>").strip()
                    
                    try:
                        value = float(value) # try to convert to float
                    except ValueError:
                        print("\n!!! Bitte gebe eine Ganz- oder Gleitkommazahl ein !!!")
                        input("\nDrücke Enter um erneut einen Wert einzugeben\n>")
                    else:
                        break # goes to next element
                

                stored_matrices.get(name).set_value(i ,j ,value) # sets Value at Element i, j

        # Show Result
        os.system("cls")
        print("Folgende Matrix wurde angelegt:")
        print(f"{name} =\n {stored_matrices.get(name)}")

        # Try Again
        print("\nMöchtes du eine weitere Matrix anlegen?(Y/N)") 
        if input(">") == "Y": pass # repeats input_matrix if Y
        else: return # return to menu

#--------------------ChangeMatrixName--------------------------#
def change_matrix_name():
    """brief: this function lets the user change the name of a matrix"""
    
    while True:
        os.system("cls") # clears screen
        print_created_matrices()

        print("\nWie heißt die Matrix, bei der der Name geändert werden soll?")
        choice = input_existing_matrix()

        if choice == NAME_EMERG_MAT: # so one cant change name and later delete the emergMat
                print(f"\n!!! Der Name der Matrix: {choice} darf nicht geändert werden !!!")

        else:
            name = input("\nAuf was soll die Matrix umbenannt werden?\n>").strip() 
            stored_matrices[name] = stored_matrices.pop(choice)
            print(f"\nDie Matrix wurde erfolgreich von {choice} auf {name} umbenannt")

        print("\nMöchtes du den Namen einer anderen Matrix änderen?(Y/N)") 
        if input(">") == "Y": pass # repeats show_matrix if Y
        else: return # return to menu

#--------------------ChangeMatrixValue-------------------------#
def change_matrix_value():
    """brief: this fuction lets the user change a given value"""

    while True:
        os.system("cls") # clears screen
        print_created_matrices()

        # input existing matrix
        print("\nBei welcher Martix soll der Wert geändert werden?")
        choice = input_existing_matrix()

        tempMat = stored_matrices.get(choice) # choice matrix is converted to object

        # input row
        os.system("cls") # clears screen
        print(f"{choice} =\n {tempMat}") # prints the selected matrix
        print("\nIn welcher Zeile der Martix soll der Wert geändert werden?")

        row = input_matrix_row(tempMat.get_rows())

        # input column
        os.system("cls") # clears screen
        print(f"{choice} =\n {tempMat}") # prints the selected matrix
        print("\nIn welcher Spalte der Martix soll der Wert geändert werden?")

        column = input_matrix_column(tempMat.get_columns())

        # input value
        os.system("cls") # clears screen
        print(f"{choice} =\n {tempMat}") # prints the selected matrix
        print(f"\nAuf welchen Wert soll das Element an Stelle {row}, {column} geändert werden?")

        while True:
            value = input(">").strip()
            try:
                value = float(value) # try to convert to float
            except ValueError:
                print("\n!!! Der Wert muss eine Ganz- oder Gleitkommzahl sein !!!")
            else: break

            print("\nBitte gebe den neuen Wert erneut ein:")

        #change Value
        tempMat.set_value(row,column,value)

        # print the result
        os.system("cls") # clears screen
        print("Die Matrix wurde auf folgendens geändert:\n")
        print(f"{choice} =\n {tempMat}") # prints the new matrix

        # ask if the user wants to repeat the process
        print("\nMöchtest du einen anderen Wert in einer Matrix ändern?(Y/N)") 
        if input(">") == "Y": pass # repeats change_matrix_value if Y
        else: return # return to menu

#-------------------------showMatrix---------------------------#
def show_matrix():
    """brief: this function lets the user see the value of a matrix"""

    while True:
        os.system("cls") # clears screen
        print_created_matrices()

        print("\nWelche Matrix möchtest du anzeigen?")
        choice = input_existing_matrix()
        os.system("cls")
        print(f"{choice} =\n {stored_matrices.get(choice)}")

        print("\nMöchtes du eine weitere Matrix anzeigen?(Y/N)") 
        if input(">") == "Y": pass # repeats show_matrix if Y
        else: return # return to menu

#----------------------printCreatedMatrices--------------------#
def print_created_matrices():
    """brief: this fuctions prints a list of all created functions"""

    print("Folgende Matrizen wurden angelegt:")
    for i in stored_matrices.keys(): print(f"- {i}") # prints a list of all matrices

#-------------------------deleteMatrix-------------------------#
def delete_matrix():
    """brief: this function lets the user delete a matrix"""

    while True:
        os.system("cls") # clears screen
        print_created_matrices()

        print("\nWelche Matrix möchtest du löschen?")
        choice = input_existing_matrix()

        # safety mechanism so that the user can always chose a matrix
        if choice == NAME_EMERG_MAT: 
            print(f"\n!!! Die Matrix: {choice} darf nicht gelöscht werden !!!")

        else:
            del stored_matrices[choice] # delets the selected matrix

            print(f"\nDie Matrix: {choice} wurde erfolgreich gelöscht")

        print("\nMöchtes du eine andere Matrix löschen?(Y/N)") 
        if input(">") == "Y": pass # repeats delete_matrix if Y
        else: return # return to menu

#-------------------------saveMatrix---------------------------#
def save_matrix(result):
    """brief: this function lets the user save a given result matrix"""
    
    print("\nMöchtest du die Ergebnismatrix speichern?(Y/N)")

    while True:
        
        if input(">").strip() == "Y":

            os.system("cls")
            print("\nUnter welchem Namen soll die Matrix gespeichert werden?")
            name = input(">").strip()

            if str(stored_matrices.get(name)) == "None": # checks if Matrix does not exist
                stored_matrices[name] = result # saves Matrix

                print(f"\nDas Ergebnis wurde erfolreich in der Matrix: {name} gespeichert")
                return #leaves the function
            else:
                print(f"\n Die Matrix: {name} existiert bereits, möchtest du diese überschreiben?(Y/N)")

                if input(">").strip() == "Y":
                    stored_matrices.update({name: result}) # replaces old Matrix with new one

                    print(f"\nDas Ergebnis wurde erfolreich in der Matrix: {name} gespeichert")
                    return #leave function
                
                else: pass

        else: return

        print("\nMöchtest du die Ergebnismatrix unter einem anderem Namen abspeichern?(Y/N)") # retry to save matrix

#===================FunctionsForOperations=====================#

#---------------------------addMatrix--------------------------#
def add_matrix():
    """"brief: this function lets the user add two matrices"""

    while True:
        os.system("cls")
        print_created_matrices()
        print("\nWelche Matrix ist der erste Summand?")
        summand1 = input_existing_matrix()
        summand1 = stored_matrices.get(summand1) # convert to object

        os.system("cls")
        print_created_matrices()
        print("\nWelche Matrix ist der zweite Summand?")
        summand2 = input_existing_matrix()
        summand2 = stored_matrices.get(summand2) # convert to object

        if( (summand1.get_columns() == summand2.get_columns())\
            and (summand1.get_rows() == summand2.get_rows()) ):

            result = summand1 + summand2

            os.system("cls")
            print(f"Das Ergebnis der Addition ist:\n{result}")

        else:
            print("\n!!! Die Matrizen konnten nicht addiert werden,da sie nicht von gleicher Größe sind !!!\n")
        
        save_matrix(result) # try to save matrix

        print("\nMöchtest du eine weitere Matrix addieren?(Y/N)") 
        if input(">") == "Y": pass # repeats add_matrix if Y
        else: return # return to menu

#---------------------------subMatrix--------------------------#
def sub_matrix():
    """"brief: this function lets the user subtract two matrices"""

    while True:
        os.system("cls")
        print_created_matrices()
        print("\nWelche Matrix ist der Minuend?")
        minuend = input_existing_matrix()
        minuend = stored_matrices.get(minuend) # convert to object

        os.system("cls")
        print_created_matrices()
        print("\nWelche Matrix ist der Subtrahend?")
        subtrahend = input_existing_matrix()
        subtrahend = stored_matrices.get(subtrahend) # convert to object

        if( (minuend.get_columns() == subtrahend.get_columns())\
            and (minuend.get_rows() == subtrahend.get_rows()) ):

            result = minuend - subtrahend

            os.system("cls")
            print(f"Das Ergebnis der Subtraktion ist:\n{result}")

        else:
            print("\n!!! Die Matrizen konnten nicht subtrahiert werden,da sie nicht von gleicher Größe sind !!!\n")
        
        save_matrix(result) # try to save matrix
            
        print("\nMöchtest du eine weitere Matrix subtrahieren?(Y/N)") 
        if input(">") == "Y": pass # repeats sub_matrix if Y
        else: return # return to menu

#---------------------------mulMatrix--------------------------#
def mul_matrix():
    """"brief: this function lets the user multiply two matrices"""

    while True:
        os.system("cls")
        print_created_matrices()
        print("\nWelche Matrix ist der erste Faktor?")
        factor1 = input_existing_matrix()
        factor1 = stored_matrices.get(factor1) # convert to object

        os.system("cls")
        print_created_matrices()
        print("\nWelche Matrix ist der zweite Faktor?")
        factor2 = input_existing_matrix()
        factor2 = stored_matrices.get(factor2) # convert to object

        if( (factor1.get_columns() == factor2.get_rows())\
            and (factor1.get_rows() == factor2.get_columns()) ):

            result = factor1 * factor2

            os.system("cls")
            print(f"Das Ergebnis der Multiplikation ist:\n{result}")

        else:
            print("\n!!! Die Matrizen konnten nicht muliplizert werden,\nda die Zeilen des ersten Faktores nicht mit den Spalten\ndes zweiten Faktors übereinstimmen (und andersherum) !!!\n")

        save_matrix(result) # try to save matrix

        print("\nMöchtest du eine weitere Matrix multiplizieren?(Y/N)") 
        if input(">") == "Y": pass # repeats mul_matrix if Y
        else: return # return to menu


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

(0) Programm beenden

Wähle eine Nummer:""")

    match input(">").strip():
        case "1": submenu_variable_manager() 
        case "2": submenu_operation_manager()
        case "3": pass
        case "4": pass
        case "0":
            print("\nBist du dir sicher, dass du das Programm schließen möchtest?(Y/N)")
            if input(">") == "Y": break
            else: pass
        case _: pass

        #TODO: Save Function for saving Matrix from addition
        #TODO: (Scalar Multiplication)
        #TODO: transpone Matrix
        #TODO: calculate determin