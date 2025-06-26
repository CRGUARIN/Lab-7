def mainMenu():
    """
    It shows the main menu and asks the user for the desired option.
    
    Args: 
        none

    Returns:
        string: the desired option
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

def menuDeleteStudent():
    print("""
------------------------------------------------
Ingrese el documento del estudiante que desea eliminar:""")

    while True:
        id = input()

        if id.isdigit():
            
            if len(id) == 10:
            
                return int(id)
            
            else:
            
                print("Ingrese un número de documento válido")

        else:
        
            print("Ingrese un número de documento válido")

