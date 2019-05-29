import sqlite3
import requests
from random import randint
import APISERVICE
import DBSERVICE
from Bebida import bebida
class APIBebida(APISERVICE.APISERVICE):
    def buscarNombre(self, drinkName):
        url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkName
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()  # DiccionarioJ con elemento de una lista
            idDrink = response_json['drinks']  # Elemento de la lista que es un diccionario

            i = 0  # variable de control para obtener los nombres de los resultados a buscar
            nombreBebidas = []  # almaceno en una lista los nombres de los resultados a buscar
            infoBebidas = []  # almaceno todos los elementos de todas las bebidas
            for clave in idDrink:
                clave = idDrink[i].get("strDrink")  # imprimo los nombres de los resultados
                nombreBebidas.append((f"Bebida {clave} numero {i}"))

                clave = idDrink[i]  # guardo cada diccionario de cada bebida
                infoBebidas.append(clave)
                i += 1

            return nombreBebidas

    def getBebida(self, bebidaElegida, drinkName):
        url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkName
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()  # DiccionarioJ con elemento de una lista
            idDrink = response_json['drinks']  # Elemento de la lista que es un diccionario

            # asignamos el valor de bebida
            id = idDrink[bebidaElegida].get("idDrink")
            nombre = idDrink[bebidaElegida].get("strDrink")
            tags = idDrink[bebidaElegida].get("strTags")
            categoria = idDrink[bebidaElegida].get("strCategory")
            alcohol = idDrink[bebidaElegida].get("strAlcoholic")
            vaso = idDrink[bebidaElegida].get("strGlass")
            instrucciones = idDrink[bebidaElegida].get("strInstructions")
            imagen = idDrink[bebidaElegida].get("strDrinkThumb")
            ingredientes = ""
            ing = 1
            while ing <= 15:
                if idDrink[bebidaElegida].get(f"strIngredient{ing}") != "" or idDrink[bebidaElegida].get(f"strIngredient{ing}") != " ":
                    ingredientes += idDrink[bebidaElegida].get(f"strIngredient{ing}")
                    ingredientes += ", "
                    ing += 1

            medidas = ""
            med = 1
            while med <= 15:
                if idDrink[bebidaElegida].get(f"strMeasure{med}") != "" or idDrink[bebidaElegida].get( f"strMeasure{med}") != " " or idDrink[bebidaElegida].get(f"strMeasure{med}") != "\n":
                    medidas += idDrink[bebidaElegida].get(f"strMeasure{med}")
                    medidas += ", "
                    med += 1

            bienElectrico = randint(5, 10)

            #creamos el objeto bebida
            b = bebida(id, nombre, tags, categoria, alcohol, vaso, instrucciones, imagen, ingredientes, medidas, bienElectrico)

            return b

class DB(DBSERVICE.DBSERVICE):
    def __init__(self, archivo):
        self.con = sqlite3.connect(archivo)
        #self.con = sqlite3.connect('El_Fieston.db')
        self.cur = self.con.cursor()

    def guardarBebida(self, bebida):
        #b = (bebida.id, bebida.nombre, bebida.tags, bebida.categoria, bebida.alcohol, bebida.vaso, bebida.instrucciones, bebida.imagen, bebida.ingredientes, bebida.medidas, bebida.bienElectrico)
        self.cur.execute("INSERT INTO favoritos VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(bebida.id,bebida.nombre, bebida.tags, bebida.categoria, bebida.alcohol, bebida.vaso, bebida.instrucciones, bebida.imagen, bebida.ingredientes, bebida.medidas, bebida.bienElectrico))
        #self.cursor.execute("INSERT INTO favoritos VALUES (?,?,?,?,?,?,?,?,?,?,?)", b)
        self.con.commit()

        return (f"Bebida guardada con extio !!! ")

    def mostrarBebidas(self):
        bMostrar = self.cur.execute("SELECT * from favoritos").fetchall()

        bebidas = []
        i = 0
        for b in bMostrar:
            bebidas.append(bebida(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10]))
            i+=1

        return bebidas

    def borrarBebida(self, nombre):
        self.cur.execute("DELETE FROM favoritos WHERE nombre = ?",(nombre,))
        self.con.commit()

        return ("Bebida Eliminada con Exito !!!")

    def actualizarBebida(self, nombre, bienElectrico):
        self.cur.execute("UPDATE favoritos SET bienElectrico= ? WHERE nombre=?",(bienElectrico, nombre))
        #print(bienElectrico,nombre)
        self.con.commit()

        return (f"La Bebida: {nombre} fue actualizada =) !!!")

if __name__ == '__main__':
    db = DB()