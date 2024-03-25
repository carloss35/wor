
class estudiante():
    def __init__(self, nombre, apellidos, grupo, edad, NIA):
       self.nombre = nombre
       self.apellidos = apellidos
       self.grupo = grupo
       self.edad = edad
       self.NIA = NIA

    def mostrar (self):
        print()
        print(f'nombre: {self.nombre}')
        print(f'apellidos: {self.apellidos}')
        print(f'grupo: {self.grupo}')
        print(f'edad: {self.edad}')
        print(f'NIA: {self.NIA}')

    def mayorDeEdad (self):
        if self.edad >= 18:
            print('Este alumno es mayor de edad')
        else:
            print('Este alumno es menor de edad')

alumno1 = estudiante("Antonio","Gómez García","4ESOA",16,12356788)
alumno1.mostrar()
print(alumno1.mayorDeEdad())


