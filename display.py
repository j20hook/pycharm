from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.screen import Screen
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField

from metodos_bbdd import *

def obtener_datos_tabla():
    list_jugadores = consulta_datos()
    datos = []

    for jug in list_jugadores:
        datos_jugador = [jug["id"],
                         jug["nombre"],
                         jug["puntos"],
                         jug["rebotes"],
                         jug["asistencias"],
                         jug["valoracion"]]

        datos.append(tuple(datos_jugador))

    return datos

def restaurar_menu(ventana, panel_botones):
    ventana.clear_widgets()
    ventana.add_widget(panel_botones)

def cargar_datos_tabla(tabla):

    #Cargar los datos
    list_jugadores = consulta_datos()

    tabla.row_data= []

    for jugador in list_jugadores:
        tabla.row_data.append(jugador)


def muestra_formulario(panel_principal):

    #1 Limpiar el panel
    panel_principal.clear_widgets()

    # 2 Crear formulario

    input_nombre = MDTextField(
        hint_text= "Nombre",
        mode="round",
        max_text_length=50,
    )

    input_puntos = MDTextField(
        hint_text="Puntos",
        mode="round",
        max_text_length=4
    )

    input_rebotes = MDTextField(
        hint_text="Rebotes",
        mode="round",
        max_text_length=4
    )

    input_asistencias = MDTextField(
        hint_text="Asistencias",
        mode="round",
        max_text_length=4
    )
    input_valoracion = MDTextField(
        hint_text="Valoración",
        mode="round",
        max_text_length=4
    )
    #3 Mostrar el formulario
    panel_principal.add_widget(crear_panel_botones(ventana, tabla, panel_principal))
    panel_principal.add_widget(input_nombre)
    panel_principal.add_widget(input_puntos)
    panel_principal.add_widget(input_rebotes)
    panel_principal.add_widget(input_asistencias)
    panel_principal.add_widget(input_valoracion)


def guardar_en_bbdd(panel_principal):

    nuevo_jugador = dict()
    nuevo_jugador["nombre"] = panel_principal.children[4].text
    nuevo_jugador["puntos"] = float(panel_principal.children[3].text)
    nuevo_jugador["rebotes"] = float(panel_principal.children[2].text)
    nuevo_jugador["asistencias"] = float(panel_principal.children[1].text)
    nuevo_jugador["valoracion"] = float(panel_principal.children[0].text)

    insertar(nuevo_jugador)


def crear_panel_botones(ventana,
                        tabla,
                        panel_principal):

    panel_botones = GridLayout(cols=6, row_force_default=True, row_default_height=70)

    boton1 = Button(text ="Cargar",
                background_color =(1, 0.7, 0, 1))
    boton1.bind(on_press=lambda a: restaurar_menu(ventana, panel_botones))

    boton2 = Button(text="Mostrar",
                    background_color =(1, 0.7, 0, 1))
    boton2.bind(on_press=lambda a: cargar_datos_tabla(tabla))

    boton3 = Button(text="Nuevo",
                    background_color =(1, 0.7, 0, 1))
    boton3.bind(on_press = lambda a: muestra_formulario(panel_principal))

    boton4 = Button(text="Guardar",
                    background_color =(1, 0.7, 0, 1))
    boton4.bind(on_press = lambda a: guardar_en_bbdd(panel_principal))


    panel_botones.add_widget(boton1)
    panel_botones.add_widget(boton2)
    panel_botones.add_widget(boton3)
    panel_botones.add_widget(boton4)


    return panel_botones


class Aplication(MDApp):
    def build(self):

        ventana = Screen(name="Jugadores ACB")

        panel_principal = GridLayout(cols=1)

        tabla = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(6, 6),
            use_pagination=True,
            check=True,
            column_data=[
                ("id", dp(20)),
                ("nombre", dp(35)),
                ("puntos", dp(20)),
                ("rebotes", dp(20)),
                ("asistencias", dp(30)),
                ("valoracion", dp(30)),
            ]
        )

        panel_botones = crear_panel_botones(ventana,
                                            tabla, panel_principal)
        ventana.add_widget(panel_principal)
        panel_principal.add_widget(panel_botones)
        panel_principal.add_widget(tabla)





        return ventana




Aplication().run()
