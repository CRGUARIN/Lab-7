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

    #Option --> Delete student
    if option == "1":
        
        st_id = intr.menuAskID("Ingrese el ID del estudiante cuyos datos desea eliminar:")
        result = lg.deleteStudent(st_id, ids, grades)

        if result == True:
            
            print(f"\nLos datos del estudiante con ID {st_id} fueron eliminados con éxito")

        else: 

            print(f"\nNo se encontró al estudiante con ID {st_id} en la base de datos.")

    #Option --> Highest grade
    if option == "2":

        st_id = intr.menuAskID("Ingrese el ID del estudiante cuya nota más alta desea conocer:")
        result = lg.bestStudentGrade(st_id, ids, grades, subjects)

        if result == False:
            print(f"\nNo se encontró al estudiante con ID {st_id} en la base de datos.")
        
        else: 
            highest_grade, subject_name = result
            print(f"""La nota más alta del estudiante con ID {st_id} fue {highest_grade} en el {subject_name}""")