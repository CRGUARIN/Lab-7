def loadStudentsData(filePath):
    """
    Receives the file's path as input and returns all the students data in
    three diferent lists

    Args:
        filePath --> (str) The file's path with the data

    Returns:
        Tuple[List(str), List[str], List(float)]
        -The first contains the subjects info
        -The second contains the student's IDs
        -The third contains the matrix with the student's grades

    Raises:
        FileNotFoundError --> If the function doesn't find the file with the
        typed path
    """
    #Opening the document
    with open(filePath, 'r') as file:
        
        try:
            
            #Reading and storing every line in a list
            lines = file.readlines()

            #The first line contain the subjects
            #We clean the line to prevent bugs and separate it to create a new list with the subjects
            subjects = lines[0].strip().split(',')

            #The second line contains the student's IDs
            #We clean the line to prevent bugs and separate it to create a new list with the subjects
            ids = lines[1].strip().split(',')

            #Creating a list that is going to contain the sublists
            grades = []

            #The remaining lines are the student's notes
            for i in range(2, len(lines)):
                
                #Separating every remaining line
                temp_line = lines[i]

                #Cleaning the current line and creating a sublist with the line's grades in string 
                clean_line = temp_line.strip().split(',')
   
                #Creating a list that is going to contain the grades of every student (individually)
                student_grades = []
                
                #Converting the grades into integers
                for note in clean_line:
                    
                    number = float(note)
                    student_grades.append(number)

                #Appending the sublist to the "main" list
                grades.append(student_grades)

            #Returning the lists inside a tuple
            return subjects, ids, grades

        except FileNotFoundError:
            print(f'Error: El archivo {filePath} no existe')

def deleteStudent(studentID, ids_list, grades_matrix):
    """
    Receives a student ID, the list with all the IDs and the matrix with the grades.
    Based on the student ID index deletes all the related data.

    Args:
        studentID --> (str) The student to be deleted
        ids_list --> (List[str]) The list with all the IDs
        grades_matrix --> (List[int]) The list with the student's grades

    Returns:
        True --> If the process is successful 
        False --> if the process is unsuccessful

    Raises:
        ValueError --> If the student ID is not found
    """
    try: 
        #Finding the student ID index
        student_index = ids_list.index(studentID)

        #Deleting all the data related with the student
        ids_list.pop(student_index)
        grades_matrix.pop(student_index)

        return True

    #If the index method doesn't find the requested ID it returns a ValueError        
    except ValueError:
        
        return False

def bestStudentGrade(studentID, ids_list, grades_matrix, subjects):
    """
    Receives an ID and returns trhe highest grade of that student

    Args:
        studentID --> (str) The student whose highest grade you want to know
        ids_list --> (List[str]) The list with all the IDs
        grades_matrix --> (List[float]) The list with all the student's grades
        subjects --> (List[str]) The list with subjects info

    Returns:
        highest_grade, subject_name --> (int, str) If the process is successful
        False --> (bool) If the process is unsuccessful

    Raises:
        ValueError --> If the function doesn't find the entered ID
    """
    try:
        
        #Find the student ID index
        student_index = ids_list.index(studentID)

        #Getting the student grades index
        student_grades = grades_matrix[student_index]

        #Find the highest grade and it's position
        #We use values that every grade overcome
        highest_grade = -1
        grade_index = -1
        
        for i in range(len(student_grades)):
            
            if student_grades[i] > highest_grade:
                highest_grade = student_grades[i]
                grade_index = i

        #Find the subject name
        subject_name = subjects[grade_index]

        #Return the highest grade and the corresponding subject
        return highest_grade, subject_name
    
    #If .index() method doesn't find the ID it returns a ValueError
    except ValueError:
        return False
