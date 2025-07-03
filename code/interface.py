def mainMenu():
    """
    It shows the main menu, asks the user for the desired option, verifies that it meets the requirements, and returns it.
    
    Args: 
        none

    Returns:
        option --> (str) The desired option
    """
    print("""

▗▄▄▖ ▄ ▗▞▀▚▖▄▄▄▄  ▄   ▄ ▗▞▀▚▖▄▄▄▄  ▄    ▐▌ ▄▄▄  
▐▌ ▐▌▄ ▐▛▀▀▘█   █ █   █ ▐▛▀▀▘█   █ ▄    ▐▌█   █ 
▐▛▀▚▖█ ▝▚▄▄▖█   █  ▀▄▀  ▝▚▄▄▖█   █ █ ▗▞▀▜▌▀▄▄▄▀ 
▐▙▄▞▘█                             █ ▝▚▄▟▌      
------------------------------------------------
Seleccione una opción:

1. Eliminar estudiante
2. Consultar la mayor nota de un estudiante
3. Ordenar y mostrar estudiantes por promedio
4. Ordenar y mostrar a los estudiantes por la 
cantidad de cursos inscritos
5. ¡1.21 gigavatios! ¡Santo cielo!
6. Salir 
""")

    while True:
        option = input("Ingrese la opción deseada: ")
        if option not in ["1", "2", "3", "4", "5", "6"]:
            print("\nIngrese una opción válida\n")
        else:
            return option

def menuAskID(message):
    """It shows the desired message, asks for an ID number and verifies that the input meets the requirements
    
    Args:
        message --> (string) What do you want to do with the ID?

    Returns
        id --> (str) The ID typed by the user
    """
    print(f"""
------------------------------------------------
{message}""")

    while True:
        id = input()

        if id.isdigit():
            
            if len(id) == 10:
            
                return id
            
            else:
            
                print("Ingrese un número de documento válido")

        else:
        
            print("Ingrese un número de documento válido")
