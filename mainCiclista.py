from Ciclista import Ciclista
ciclista = Ciclista

respuestas = []

contador = 1
respuesta = {}

while (contador <=3):

    ciclista.__nombre = input("ingrese nombre: ")
    ciclista.__edad = int(input("ingrese edad: "))
    ciclista.__pais = input("ingrese pais: ")
    ciclista.__tiempo = int(input("ingrese tiempo: "))

    respuesta['nombre'] = ciclista.__nombre
    respuesta['edad'] = ciclista.__edad
    respuesta['pais'] = ciclista.__pais
    respuesta['tiempo'] = ciclista.__tiempo

    respuestas.append(respuesta)
    contador +=1

tiempoMayor = 1000
for index , value in enumerate(respuestas):
   
   if(ciclista.__tiempo < tiempoMayor):
       tiempoMayor = ciclista.__tiempo
       print(respuesta)
    