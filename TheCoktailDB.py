import requests
import sqlite3
import APISERVICE
import APICLASS

def buscar(apiclas):
    n = input("Nombre de la Bebida: ")
    buscar = apiclas.buscarNombre(n)
    print("Bebidas encontradas: ")
    print(buscar)
    be = int(input("Elige una Bebida por su numero: "))
    mostrr = apiclas.getBebida(be, n)
    print(mostrr)
    return mostrr

def guardar(apiclas2, bebida):
    print(apiclas2.guardarBebida(bebida))

def mostrarLista(apiclas2):
    print("Aqui tu lista de Favoritos !!! ")
    #print(apiclas2.mostrarBebidas())
    b = 0
    lista = apiclas2.mostrarBebidas()
    for i in lista:
        print(f"Numero {b} -> "+i.nombre)
        b+=1
    return lista

def mostrarLista2(apiclas2):
    # con este metodo muestro la lista sin imprimir
    lista = apiclas2.mostrarBebidas()
    return lista

def elegirLista(apiclas2):
    be = int(input("Elige una Bebida por su numero: "))
    lista = mostrarLista2(apiclas2)

   # if lista[be].tags != None:
    #    return str(f"Tu bebida es:" + "\n" + f"Nombre -> {lista[be].nombre}" + "\n" + f"Tags -> {lista[be].tags}" + "\n" + f"Categoria -> {lista[be].categoria}" + "\n" + f"Alcohol -> {lista[be].alcohol}" + "\n" + f"Vaso -> {lista[be].vaso}" + "\n" + f"Instrucciones -> {lista[be].instrucciones}" + "\n" + f"Imagen -> {lista[be].imagen}" + "\n" + f"Ingredientes -> {lista[be].ingredientes}" + "\n" + f"Medidas -> {lista[be].medidas}" + "\n" + f"Te pones Bien Electrico con -> {lista[be].bienElectrico}")
    #if lista[be].tags == None:
     #   return str(f"Tu bebida es:" + "\n" + f"Nombre -> {lista[be].nombre}" + "\n"  + f"Categoria -> {lista[be].categoria}" + "\n" + f"Alcohol -> {lista[be].alcohol}" + "\n" + f"Vaso -> {lista[be].vaso}" + "\n" + f"Instrucciones -> {lista[be].instrucciones}" + "\n" + f"Imagen -> {lista[be].imagen}" + "\n" + f"Ingredientes -> {lista[be].ingredientes}" + "\n" + f"Medidas -> {lista[be].medidas}" + "\n" + f"Te pones Bien Electrico con -> {lista[be].bienElectrico}")
    return lista[be]

def actualizar(apiclas2, nombre, bienElectrico):
    actu = apiclas2.actualizarBebida(nombre, bienElectrico)
    return actu

def borrar(apiclas2, nombre):
    borr = apiclas2.borrarBebida(nombre)
    return borr

def main():
    apiclas = APICLASS.buscarNombre()
    apiclas2 = APICLASS.guardarBebida()
    print("Bienvenido al Sabor, Elige una opcion: ")
    opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida "+"\n"+"2 -> Mostrar Bebidas Guardadas "+ "\n3 -> Actualizar Bebida " +"\n4 -> Borrar Bebida" +"\n"+"5 -> Salir " + "\nOpcion: "))
    cont = 0
    while cont == 0:
        if opcion == 1:
            #muestro la bebida bde me guarda el objeto bebida
            bde = buscar(apiclas)
            print("Guardar Bebida ?")
            gb = int(input("0 -> Si "+"\n"+"1 -> No " + "\nOpcion: "))
            if gb == 0:
                #guardo la bebida
                guardar(apiclas2, bde)
                opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida "+"\n"+"2 -> Mostrar Bebidas Guardadas "+ "\n3 -> Actualizar Bebida " +"\n4 -> Borrar Bebida" +"\n"+"5 -> Salir " + "\nOpcion: "))
            elif gb == 1:
                #muestro el meno de nuevo porque no se guardo la bebida
                opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida "+"\n"+"2 -> Mostrar Bebidas Guardadas "+ "\n3 -> Actualizar Bebida " +"\n4 -> Borrar Bebida" +"\n"+"5 -> Salir " + "\nOpcion: "))
            else:
                #vuelvo a pedir que me den una opcion porque no me dieron una valida
                print("Introdusca una opcion valida")
                gb = int(input("0 -> Si " + "\n" + "1 -> No" + "\nOpcion: "))

        elif opcion == 2:
            #aqui voy a mostrar los puros nombres de la lista que tengo en la base dados
            mB = mostrarLista(apiclas2)
            print("Quieres ver una Bebida? ")
            opc = int(input("0 -> Si "+"\n"+"1 -> No " + "\nOpcion: "))
            if opc == 0:
                #muestro la bebida elegida
                mb = elegirLista(apiclas2)
                print(mb)
            elif opc == 1:
                opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida "+"\n"+"2 -> Mostrar Bebidas Guardadas "+ "\n3 -> Actualizar Bebida " +"\n4 -> Borrar Bebida" +"\n"+"5 -> Salir " + "\nOpcion: "))
            else:
                print("Introdusca una opcion valida")
                opc = int(input("0 -> Si " + "\n" + "1 -> No " + "\nOpcion: "))

        elif opcion == 3:
            #Actualizo una Bebida
            mB = mostrarLista(apiclas2)
            #muestro la bebida elegida
            mb = elegirLista(apiclas2)
            #pido el valor del campo a actualziar
            bienElectrico = int(input("Ahora con cuantas te pones Bien Electrico :0 ?: "))
            ac = actualizar(apiclas2, mb.nombre, bienElectrico)
            print(ac)
            print("Volver al MENU ")
            opc = int(input("0 -> Si "+"\nOpcion: "))
            if opc == 0:
                opcion = int(input("MENU" + "\n" + "1 -> Buscar Bebida " + "\n" + "2 -> Mostrar Bebidas Guardadas " + "\n3 -> Actualizar Bebida " + "\n4 -> Borrar Bebida" + "\n" + "5 -> Salir " + "\nOpcion: "))
            else:
                print("Introdusca una opcion valida")
                opc = int(input("0 -> Si " + "\n" + "1 -> No " + "\nOpcion: "))

        elif opcion == 4:
            #borro una Bebida
            mB = mostrarLista(apiclas2)
            # muestro la bebida elegida
            mb = elegirLista(apiclas2)
            bor = borrar(apiclas2, mb.nombre)
            print(bor)
            print("Volver al MENU ")
            opc = int(input("0 -> Si " + "\nOpcion: "))
            if opc == 0:
                opcion = int(input("MENU" + "\n" + "1 -> Buscar Bebida " + "\n" + "2 -> Mostrar Bebidas Guardadas " + "\n3 -> Actualizar Bebida " + "\n4 -> Borrar Bebida" + "\n" + "5 -> Salir " + "\nOpcion: "))
            else:
                print("Introdusca una opcion valida")
                opc = int(input("0 -> Si " + "\n" + "1 -> No " + "\nOpcion: "))

        elif opcion == 5:
           #mato el sistema :D
           exit()
        else:
            print("Introdusca una opcion valida")
            opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida "+"\n"+"2 -> Mostrar Bebidas Guardadas "+ "\n3 -> Actualizar Bebida " +"\n4 -> Borrar Bebida" +"\n"+"5 -> Salir " + "\nOpcion: "))

if __name__ == '__main__':
    main();