from Ciclista import Ciclista
ciclista = Ciclista

respuestas = []

contador = 1


while (contador <=2):

    ciclista.nombre = input("ingrese nombre: ")
    ciclista.edad = int(input("ingrese edad: "))
    ciclista.pais = input("ingrese pais: ")
    ciclista.tiempo = int(input("ingrese tiempo: "))

  

    respuestas.append(ciclista)
    contador +=1

tiempoMayor = 1000
for index , value in enumerate(respuestas):
   
   if(ciclista.tiempo < tiempoMayor):
       tiempoMayor = ciclista.tiempo
       print(f"el menor tiempo menor es {tiempoMayor} ")
    