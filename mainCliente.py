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
        client={} 
        cliente.__nombre = input("ingrese nombre: ")
        cliente.__apellido = input("ingrese apellido: ")
        cliente.__cedula = int(input("ingrese cedula: "))
        cliente.__ciudad = input("ingrese ciudad: ")
        cliente.__numCuenta = int(input("ingrese numero de cuenta: "))
        cliente.__saldo = int(input("ingrese saldo: "))

        client['nombre'] =  cliente.__nombre 
        client['apellido'] = cliente.__apellido
        client['cedula'] = cliente.__cedula
        client['ciudad'] = cliente.__ciudad
        client['numCuenta'] =cliente.__numCuenta
        client['saldo'] = cliente.__saldo

        clientes.append(client["saldo"])
    elif(opcion == 2):
        print(clientes)
    elif(opcion == 3):
        ingresar = int(input("ingrese valor: "))
        for i in clientes:
           suma = i + ingresar
        clientes = suma
    elif(opcion == 4):
        retirar = int(input("ingrese valor: "))
        for e in clientes:
           resta = e - retirar
        clientes = resta
    elif(opcion == 5):
        break
    else:   
        print("digita una opcion valida")
else:
    print("para ahi")  
   


   
  