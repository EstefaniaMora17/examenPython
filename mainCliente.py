from Ciclista import Ciclista
from Cliente import Cliente
cliente = Cliente



opcion = 1
print("Meno ")
print("**********")
print("1. agregar informacion ")
print("2. consultar saldo")
print("3. ingresar dinero")
print("4. retirar dinero")
print("5. salir")
clientes=[]


while(opcion != 0):
    opcion=int(input("digite un numero: "))
    if(opcion == 1):
        cliente=Cliente() #crear el objeti de ckase Cliente
        # cliente.nombre = input("ingrese nombre: ")
        # cliente.apellido = input("ingrese apellido: ")
        # cliente.cedula = int(input("ingrese cedula: "))
        # cliente.ciudad = input("ingrese ciudad: ")
        cliente.numCuenta = int(input("ingrese numero de cuenta: "))
        cliente.saldo = int(input("ingrese saldo: "))

      

        clientes.append(cliente)
    elif(opcion == 2):

        for cliente in clientes:
            print(f"su saldo es {cliente.saldo}")
        
    elif(opcion == 3):
        ingresar = int(input("ingrese valor: "))
        suma = cliente.saldo + ingresar
        cliente.saldo = suma
        print(f"ingresaste {ingresar}")
    elif(opcion == 4):
        retirar = int(input("ingrese valor: "))
        if(retirar <= cliente.saldo):
            resta =   cliente.saldo - retirar 
            cliente.saldo = resta
            print(f"retiraste {retirar}")
        else:
            print("no tiene saldo sufiente ")
        
    elif(opcion == 5):
        break
    else:   
        print("digita una opcion valida")
else:
    print("para ahi")  
   


   
  