class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}. ¡Felicidades!")
        else:
            print(f"{self.nombre} ha reprobado con una nota de {self.nota}. ¡Ánimo para la próxima!")

alumno1 = Alumno("Juan", 8)

alumno1.imprimir_info()

alumno1.resultado()