#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos
#su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
#con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    #función con los resultados
    def resultados(self):
        if self.nota >= 5: 
            print(self.nombre + ", tu nota es " + str(self.nota) + ", has aprobado.")
        else:
            print(self.nombre + ", tu nota es " + str(self.nota) + ", no has aprobado.")

#Creo los objetos, con lo que inicializo la clase 
alumno1= Alumno("Cristina",3)
alumno2= Alumno("Maximilian",7)
alumno3= Alumno("Jorge",5)

#Llamamos la funcion de resultados
alumno1.resultados()
alumno2.resultados()
alumno3.resultados()


