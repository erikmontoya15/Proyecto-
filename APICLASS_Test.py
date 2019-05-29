import unittest
import sqlite3
import os
from Bebida import bebida
from unittest.mock import patch
from unittest.mock import MagicMock
from APICLASS import DB
from APICLASS import APIBebida

#Pruebas Unitarias
class TestAPICLASS(unittest.TestCase):
    #Prueba Unitaria en donde me conecto a la API TheCocktailDB, enlistando las bebidas encontradas
    @patch('requests.get')
    def test_buscarNombre(self, mock_get):
        test_cases = (
            ("Vodka", ['Bebida Long vodka numero 0', 'Bebida Vodka Fizz numero 1', 'Bebida Coffee-Vodka numero 2', 'Bebida Vodka Martini numero 3', 'Bebida Vodka Russian numero 4', 'Bebida Vodka And Tonic numero 5'], lambda: {"drinks": [{"strDrink": "Long vodka"}, {"strDrink": "Vodka Fizz"}, {"strDrink": "Coffee-Vodka"}, {"strDrink": "Vodka Martini"}, {"strDrink": "Vodka Russian"}, {"strDrink": "Vodka And Tonic"}]}),
            ("Whiskey", ['Bebida Whiskey Sour numero 0'], lambda: {"drinks":[ {"strDrink": "Whiskey Sour"}]}),
            ("Manhattan", ['Bebida Manhattan numero 0'], lambda: {"drinks": [{"strDrink": "Manhattan"}]})
        )

        buscar = APIBebida()

        for entrada,esperado,funcion in test_cases:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json = funcion

            salida_real = buscar.buscarNombre(entrada)
            self.assertEqual(salida_real, esperado)

    #Prueba Unitaria en donde busco una bebida conectandome a la API TheCocktailDB y lo seleccione, para despudes crear un objeto bebida
    '''@patch('requests.get')
    def test_getBebida(self, mock_get):
        test_cases = (
            (0, "Mojito", lambda: {"drinks": [{"idDrink": 11000}, {"strDrink": "Mojito"}, {"strTags": "IBA,ContemporaryClassic,Alcoholic,USA"}, {"strCategory": "Cocktail"}, {"strAlcoholic": "Alcoholic"}, {"strGlass": "Highball glass"}, {"strInstructions": "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw."}, {"strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg"}, {"strIngredient1": "Light rum"}, {"strIngredient2": "Lime"}, {"strIngredient3": "Sugar"}, {"strIngredient4": "Mint"}, {"strIngredient5": "Soda water"}, {"strMeasure1": "2-3 oz "}, {"strMeasure2": "Juice of 1 "}, {"strMeasure3": "2 tsp "}, {"strMeasure4": "2-4 "}]}, bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10)),
            #("Margarita", 0, bebida(11007, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic", "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.", "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg", "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , ", "1 1/2 oz , 1/2 oz , 1 oz , , , , , , , , , , , , , ", 9)),
            #("Tequila", 1, bebida(12370, "Tequila Sour", "None", "Ordinary Drink", "Alcoholic", "Whiskey sour glass", "Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.", "https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg", "Tequila, Lemon, Powdered sugar, Lemon, Cherry, , , , , , , , , , , ", "2 oz , Juice of 1/2 , 1 tsp , 1/2 slice , 1 ,  ,  ,  ,  ,  , , , , , , ", 10))
        )

        buscar = APIBebida()

        for entradaNumero,entradaNombre, funcion, esperado in test_cases:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json = funcion
            salida_real = buscar.getBebida(entradaNumero, entradaNombre)
            #print(type(salida_real.id))
            #print(esperado.id)
            self.assertEqual(salida_real.id, esperado.id)'''

#Pruebas de Integracion
class TestAPICLASSI(unittest.TestCase):
    #Crear la base y darle valores
    def setUp(self):
        self.con = sqlite3.connect("TestEl_Fieston.db")
        cur = self.con.cursor()
        self.db = DB('TestEl_Fieston.db')
        cur.execute('''CREATE TABLE IF NOT EXISTS favoritos
            (id Integer,nombre Text,tags Text,categoria Text,alcohol Text,vaso Text,instrucciones Text,imagen Text,ingredientes Text,medidas Text,bienElectrico Integer)  ''')

        self.db.guardarBebida(bebida(12370, "Tequila Sour", "None", "Ordinary Drink", "Alcoholic", "Whiskey sour glass", "Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.", "https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg", "Tequila, Lemon, Powdered sugar, Lemon, Cherry, , , , , , , , , , , ", "2 oz , Juice of 1/2 , 1 tsp , 1/2 slice , 1 ,  ,  ,  ,  ,  , , , , , , ", 10))
        self.db.guardarBebida(bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7))
        self.db.guardarBebida(bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10))
        self.db.guardarBebida(bebida(12770, "Iced Coffee", "None", "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , ", "1/4 cup instant , 1/4 cup , 1/4 cup hot , 4 cups cold ,  ,  ,  ,  ,  , , , , , , , ", 7))
        self.db.guardarBebida(bebida(11007, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic", "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.", "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg", "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , ", "1 1/2 oz , 1/2 oz , 1 oz , , , , , , , , , , , , , ", 9))

    #ELIMINAR BASE DE DATOS
    def tearBorrarDB(self):
        self.con.close()
        self.db.con.close()
        os.remove("TestEl_Fieston.db")

    #ACTUALIZAR BEBIDAS
    def testActualizar(self):
        self.db.actualizarBebida("Margarita", 8)
        nombre = "Margarita"
        salida_esperada = self.con.execute("select * from favoritos where nombre = ('{}')".format(nombre))
        cursor = salida_esperada.fetchone()
        l = []
        for row in cursor:
            l.append(row)

        salida_esperada3 = bebida(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10])
        real = bebida(11000, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic",
                      "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.",
                      "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg",
                      "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , ",
                      "1 1/2 oz , 1/2 oz , 1 oz , , , , , , , , , , , , , ", 8)
        sal = (salida_esperada3.bienElectrico, salida_esperada3.nombre)
        re = (real.bienElectrico, real.nombre)
        self.assertEqual(sal, re)
    #ELIMINAR BEBIDAS
    def testELIMARBEBIDA(self):
        self.db.borrarBebida("Long vodka")
        nombre = "Long vodka"
        borrado = self.con.execute("SELECT * FROM favoritos where nombre = ('{}')".format(nombre))
        cursor = borrado.fetchone()
        #print(type(cursor))
        self.assertIsNone(cursor)

    #Agrego una bebida
    def testAGREGARBEBIDA(self):
        self.db.guardarBebida(bebida(13196, "Long vodka", "None", "Ordinary Drink", "Alcoholic", "Highball glass", "Shake a tall glass with ice cubes and Angostura, coating the inside of the glass. Por the vodka onto this, add 1 slice of lime and squeeze juice out of remainder, mix with tonic, stir and voila you have a Long Vodka", "https://www.thecocktaildb.com/images/media/drink/9179i01503565212.jpg", "Vodka, Lime, Angostura bitters, Tonic water, Ice, , , , , , , , , , , ", "5 cl , 1/2 , 4 dashes , 1 dl Schweppes , 4 ,  ,  ,  ,  ,  , , , , , , ", 7))
        real =bebida(13196, "Long vodka", "None", "Ordinary Drink", "Alcoholic", "Highball glass", "Shake a tall glass with ice cubes and Angostura, coating the inside of the glass. Por the vodka onto this, add 1 slice of lime and squeeze juice out of remainder, mix with tonic, stir and voila you have a Long Vodka", "https://www.thecocktaildb.com/images/media/drink/9179i01503565212.jpg", "Vodka, Lime, Angostura bitters, Tonic water, Ice, , , , , , , , , , , ", "5 cl , 1/2 , 4 dashes , 1 dl Schweppes , 4 ,  ,  ,  ,  ,  , , , , , , ", 7)
        nombre = "Long vodka"
        salida_esperada = self.con.execute("select * from favoritos where nombre = ('{}')".format(nombre))
        cursor = salida_esperada.fetchone()
        l = []
        for row in cursor:
            l.append(row)

        salida_esperada2 = bebida(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10])
        salida = (salida_esperada2.id, salida_esperada2.nombre, salida_esperada2.tags, salida_esperada2.categoria, salida_esperada2.alcohol, salida_esperada2.vaso, salida_esperada2.instrucciones, salida_esperada2.imagen, salida_esperada2.ingredientes, salida_esperada2.medidas, salida_esperada2.bienElectrico)
        vreal = (real.id, real.nombre, real.tags, real.categoria, real.alcohol, real.vaso, real.instrucciones, real.imagen, real.ingredientes, real.medidas, real.bienElectrico)
        self.assertEqual(salida, vreal)

    #Muestro las bebidas
    def testMostrarTodo(self):
        salida_esperada = [bebida(12370, "Tequila Sour", "None", "Ordinary Drink", "Alcoholic", "Whiskey sour glass", "Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.", "https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg", "Tequila, Lemon, Powdered sugar, Lemon, Cherry, , , , , , , , , , , ", "2 oz , Juice of 1/2 , 1 tsp , 1/2 slice , 1 ,  ,  ,  ,  ,  , , , , , , ", 10),
                bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7),
                bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10),
                bebida(12770, "Iced Coffee", "None", "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , ", "1/4 cup instant , 1/4 cup , 1/4 cup hot , 4 cups cold ,  ,  ,  ,  ,  , , , , , , , ", 7),
                bebida(11007, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic", "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.", "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg", "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , ", "1 1/2 oz , 1/2 oz , 1 oz , , , , , , , , , , , , , ", 9)]

        a = self.db.mostrarBebidas()
        self.assertEqual(salida_esperada[0], a[0])
        i=0
        for x in salida_esperada:
            self.assertEqual(salida_esperada[i], a[i])
            i+=1

    #Busco una bebida conectandome a la API TheCocktailDB, enlistando las bebidas encontradas
    def testBUSCARBEBIDA(self):
        self.api = APIBebida()
        nombre = "Vodka"
        salida_esperada =['Bebida Long vodka numero 0', 'Bebida Vodka Fizz numero 1', 'Bebida Coffee-Vodka numero 2', 'Bebida Vodka Martini numero 3', 'Bebida Vodka Russian numero 4', 'Bebida Vodka And Tonic numero 5']
        real = self.api.buscarNombre(nombre)
        self.assertEqual(salida_esperada, real)

    #Busco una bebida conectandome a la API TheCocktailDB y lo seleccione, para despudes crear un objeto bebida
    def testCREARBEBIDA(self):
        self.api = APIBebida()
        nombre = "Long vodka"
        numero = 0
        salida_esperada =bebida(13196, "Long vodka", "None", "Ordinary Drink", "Alcoholic", "Highball glass", "Shake a tall glass with ice cubes and Angostura, coating the inside of the glass. Por the vodka onto this, add 1 slice of lime and squeeze juice out of remainder, mix with tonic, stir and voila you have a Long Vodka", "https://www.thecocktaildb.com/images/media/drink/9179i01503565212.jpg", "Vodka, Lime, Angostura bitters, Tonic water, Ice, , , , , , , , , , , ", "5 cl , 1/2 , 4 dashes , 1 dl Schweppes , 4 ,  ,  ,  ,  ,  , , , , , , ", 7)
        real = self.api.getBebida(numero, nombre)
        self.assertEqual(type(salida_esperada), type(real))
        self.assertEqual(salida_esperada.id, int(real.id))

if __name__ == '__main__':
    unittest.main()