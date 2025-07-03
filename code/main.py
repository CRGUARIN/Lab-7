#Importing the functions
import logic as lg
import interface as intr
import plots as pl

#Loading data and storing every list inside a variable
subjects, ids, grades = lg.loadStudentsData("data/notas_estudiantes.csv")

#Creating the main cycle
while True:

    #Showing the main menu and storing the option
    option = intr.mainMenu()