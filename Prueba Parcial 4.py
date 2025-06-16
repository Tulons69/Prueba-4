import re

compradores = {
    "Concepcion": {}, "Puente_Alto": {}, "Valparaiso": {}, "Viña_del_Mar": {}}

Stock = { "Concepcion":500,"Puente_Alto":1300,"Valparaiso":100, "Viña_del_Mar":50}

def Validar_Codigo(codigo):
    return (len(codigo) >= 6 and any(c.isupper() for c in codigo) and any(c.isdigit()for c in codigo) and "" not in codigo)
def Comprar_Concepcion():
    nombre = input ("Ingrese Nombre del Comprador: ")
    if nombre in compradores ["Concepcion"]:
        print("Nombre ya Registrado")
        return
    codigo = input("Ingrese codigo de confirmacion: ")
    if not Validar_Codigo:
        print("Codigo Invalido")
        return
    if Stock ["Concepcion"] <= 0:
        print("No hay stock disponible")
        return
    compradores["Concepcion"][nombre] = codigo
    Stock["Concepcion"] -=1
    print("Compra Registrada Con Exito")
def Comprar_Puente_Alto():
    nombre = input("Ingrese el nombre del comprador: ")
    if nombre in compradores["Puente_Alto"]:
        print("Nombre ya registrado")
        return
    Cantidad = int(input("Ingrese Cantidad de entradas(Max 3): "))
    if Cantidad > 3 or Cantidad <= 0:
        print("Cantidad no Permitida")
        return
    if Stock["Puente_Alto"] < Cantidad:
        print("Stock insuficiente")
        return
    compradores["Puente_Alto"][nombre] = Cantidad
    Stock ["Puente_Alto"] -= Cantidad
    print("Compra Registrada exitosamente")
def Comprar_Valparaiso():
    nombre = input("Ingrese nombre del Comprador: ")
    if nombre in compradores["Valparaiso"]:
        print("Nombre ya Registrado")
        return
    tipo = input("Ingrese tipo de entrada: ")
    if tipo.upper() != "G":
        print("Tipo de entrada invalido")
        return
    if Stock["Valparaiso"] <= 0:
        print("No hay Stock disponible")
        return
    compradores["Valparaiso"][nombre] = tipo.upper()
    Stock["Valparaiso"] -=1
    print("Compra registrada exitosamente")
def Compra_Viña_del_Mar():
    nombre = input("Ingrese el Nombre del comprador:")
    if nombre in compradores ["Viña_del_Mar"]:
        print("Nombre ya registrado")
        return
    tipo = input("Ingrese tipo de entrada (Sun/Ni): ")
    if tipo not in ("Sun", "Ni"):
        print("Tipo invalido")
        return
    if Stock["Viña_del_Mar"] <= 0:
        print("No hay Stock disponible")
        return
    compradores["Viña_del_Mar"][nombre] = tipo 
    Stock["Viña_del_Mar"] -= 1
    print("Compra registrada exitosamente")
def menu():
    while True:
        print("\n Totem autoservicio gira los fortificados rock and chile in chile")
        print("1.- Comprar entradas en Concepcion")
        print("2.- Comprar entradas en Puente alto")
        print("3.- Comprar entrada en Muelle Baron, Valparaiso")
        print("4.- Comprar entradas en muelle vergara, Viña del mar") 
        print("5.- Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion =="1":
            Comprar_Concepcion()
        elif opcion =="2":
            Comprar_Puente_Alto()
        elif opcion =="3":
            Comprar_Valparaiso()
        elif opcion =="4":
            Compra_Viña_del_Mar()
        elif opcion == "5":
            print("Programa Terminado...")
            break
        else:
            print("Debe ingresar una opcion valida!!")
menu()

