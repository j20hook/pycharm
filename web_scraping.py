import requests
import bs4
def scraping_acb():
    pagina = requests.get("https://www.acb.com/estadisticas-individuales/PUNTOS/temporada_id/2022/fase_id/107")

    soup = bs4.BeautifulSoup(pagina.content,"html.parser")

    jugadores = soup.find_all("tr", {"class":"par"})

    lista_jugadores = []

    plantilla = {
        "nombre": None,
        "puntos": None,
        "asistencias": None,
        "rebotes": None,
        "valoracion": None,
    }

    # Añadimos el for de los jugadores y los puntos
    for jugador in jugadores:
        dic_jugador = plantilla.copy()
        nombre = jugador.find("span", {"class":"nombre_corto"}).text
        dic_jugador["nombre"]=nombre
        puntos = float(jugador.find("td" , {"class":"borde_derecho apartado_seleccionado"}).text.replace(",","."))
        dic_jugador["puntos"] = puntos
        rebotes = float(jugador.find_all("td", {"class": "borde_derecho"})[14].text.replace(",","."))
        dic_jugador["rebotes"] = rebotes
        asistencias = float(jugador.find_all("td", {"class": "borde_derecho"})[15].text.replace(",","."))
        dic_jugador["asistencias"] = asistencias
        valoracion = float(jugador.find_all("td", {"class": "borde_derecho"})[24].text.replace(",","."))
        dic_jugador["valoracion"] = valoracion
        lista_jugadores.append(dic_jugador)

    print(lista_jugadores)
    return lista_jugadores
