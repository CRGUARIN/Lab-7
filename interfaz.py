def mainMenu():
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
