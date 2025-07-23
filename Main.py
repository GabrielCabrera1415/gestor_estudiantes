from os import system
from Clases import *


def recibir():
    nombre = input("Nombre del estudiante: ")
    return nombre

def calificaciones():
    lista = []
    cantidad = int(input("¿Cuántas calificaciones quieres agregar?: "))
    for i in range(cantidad):        
        while True:     
            calificacion = float(input("Calificación a agregar: "))
            if calificacion <= 10  and calificacion >= 0:
                lista.append(calificacion)
                break    
            else:
                system("cls")
    return lista       

def buscar(nombre, grupo):
    for i in range(len(grupo.Estudiantes)):
        if nombre == grupo.Estudiantes[i].Nombre:
            print(f"Estudiante {nombre} encontrado en el grupo.")
            return grupo.Estudiantes[i]
    # Este print y return solo se ejecutan si el bucle termina sin encontrar nada
    print("Estudiante no encontrado")
    return None

def main():
    MiGrupo = Grupo()

    while True:
        print("=== Menú ===")
        print("1. Agregar Estudiante")
        print("2. Mostrar todos los estudiantes")
        print("3. Mostrar al mejor promedio")
        print("4. Agregar calificación a estudiante")
        print("5. Salir\n")
        opcion = input("Selecciona una opción: ")
        print("\n")

        match opcion:
            
            case "1":
                system("cls")
                nombre = recibir()
                matricula = int(input("Matricula del estudiante: "))
                calificaciones = []     
                alumno = Estudiante(nombre,matricula,calificaciones) #creamos el objeto estudiante para agregarlo
                MiGrupo.agregar_estudiante(alumno)

            case "2":
                system("cls")
                MiGrupo.mostrar_todos()

            case "3":
                system("cls")
                MiGrupo.mejor_promedio()

            case "4":
                system("cls")
                nombre = recibir()
                calif = calificaciones()
                alumno = buscar(nombre,MiGrupo)
                if alumno is not None:
                    alumno.agregar_calificacion(calif)
                    print(f"Calificación {calif} agregada a {alumno.Nombre}.")
                else:
                    print(f"Error: Estudiante '{nombre}' no encontrado. No se pudo agregar la calificación.")
                system("cls")

            case "5":
                MiGrupo.salir()
                system("cls")

            case _:
                system("cls")
                print("Opción no válida.\n")




if __name__ == "__main__":
    main()
