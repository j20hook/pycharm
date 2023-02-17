import mysql.connector as db
from web_scraping import scraping_acb

def insertar_bbdd():

    lista_jugadores = scraping_acb()

    conexion = db.connect(host='localhost',
                          port=3306,
                          database='acb',
                          user='root',
                          password='1234',
                          autocommit=True)


    cursor = conexion.cursor()

    cursor.execute("delete from estadisticas where id is not null")

    cursor.execute("alter table estadisticas auto_increment=1")
    script_insert = "insert into estadisticas (nombre, puntos, rebotes, asistencias, valoracion)" \
                        "values (%s,%s,%s,%s,%s)"


    for jugador in lista_jugadores:

        cursor.execute(script_insert,(jugador["nombre"],
                                          jugador["puntos"],
                                          jugador["rebotes"],
                                          jugador["asistencias"],
                                          jugador["valoracion"]))

    print("Datos volcados correctamente")

def consulta_datos():

    #Abrir conexion
    conexion = db.connect(host='localhost',
                          port=3306,
                          database='acb',
                          user='root',
                          password='1234',
                          autocommit=True)

    #Lista
    list_jugadores = []

    #Abrir cursor
    cursor = conexion.cursor()

    #Script de bd
    consulta = "select * from estadisticas"

    #Ejecuto la consulta
    cursor.execute(consulta)

    for dato in cursor.fetchall():
        jugador = tuple([dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]])
        list_jugadores.append(jugador)

    return list_jugadores

