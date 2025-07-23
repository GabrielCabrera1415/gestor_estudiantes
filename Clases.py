from os import system

class Estudiante:
    
    def __init__(self,Nombre:str, Matricula:int, Calificaciones:list):
        self.Nombre = Nombre
        self.Matricula = Matricula
        self. Calificaciones = Calificaciones
        
    def agregar_calificacion(self,calificacion):
        self.Calificaciones.extend(calificacion)

    def calcula_promedio(self):
        if self.Calificaciones == []:
            promedio = 0 
        else:
            promedio = sum(self.Calificaciones)/len(self.Calificaciones)
        return promedio

    def mostrar_informacion(self):
        print("Alumno: ",self.Nombre)
        print("Matricula: ",self.Matricula)
        print("Promedio",self.calcula_promedio())



class Grupo:

    def __init__(self):
        self.Estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.Estudiantes.append(estudiante)
        system("cls")

    def mostrar_todos(self):
        if self.Estudiantes != []:
            print("Estudiantes: \n")
            for estudiante in self.Estudiantes:
                estudiante.mostrar_informacion()
                print("\n") 
            input()
            system("cls")

        else:
            print("No hay alumnos que mostrar")
            input()
            system("cls")

    def mejor_promedio(self):
        if not self.Estudiantes:
            print("No hay estudiantes en el grupo para calcular el mejor promedio.")
            input("Presiona Enter para continuar...")        
            system("cls")
            return            

        primer_estudiante = self.Estudiantes[0]
        mejor_promedio_encontrado = primer_estudiante.calcula_promedio()
        nombre_mejor_alumno = primer_estudiante.Nombre
        matricula_mejor_alumno = primer_estudiante.Matricula

        for estudiante in self.Estudiantes[1:]: # Iterar desde el segundo elemento
            promedio_actual_estudiante = estudiante.calcula_promedio()
            if promedio_actual_estudiante > mejor_promedio_encontrado:
                mejor_promedio_encontrado = promedio_actual_estudiante
                nombre_mejor_alumno = estudiante.Nombre
                matricula_mejor_alumno = estudiante.Matricula

                # 5. Imprimir el resultado final
        print(f"El mejor promedio es del alumno {nombre_mejor_alumno} con matrícula: {matricula_mejor_alumno} y el promedio es {mejor_promedio_encontrado}")
        input("Presiona Enter para continuar...")        
        system("cls")

    def salir(self):
        exit()





