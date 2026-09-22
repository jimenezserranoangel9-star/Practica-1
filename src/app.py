# src/app.py
import flet as ft
from lenguajes import (
    concatenar_cadenas, potencia_cadena, inversion_cadena, longitud_cadena,
    concatenar_lenguajes, union_lenguajes, interseccion_lenguajes,
    diferencia_lenguajes, potencia_lenguaje
)

def main(page: ft.Page):
    page.title = "Práctica 1 - Operaciones sobre Cadenas y Lenguajes"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # Componentes para Operaciones con Cadenas
    txt_cadena1 = ft.TextField(label="Cadena 1 (u)", value="hola", width=300)
    txt_cadena2 = ft.TextField(label="Cadena 2 (v)", value="mundo", width=300)
    txt_potencia_k = ft.TextField(label="Exponente (n)", value="3", width=150)
    res_cadenas = ft.Text(value="Resultados de Cadenas aparecerán aquí", size=16, weight=ft.FontWeight.BOLD)

    def calcular_cadenas(e):
        u = txt_cadena1.value or ""
        v = txt_cadena2.value or ""
        try:
            n = int(txt_potencia_k.value or 0)
        except ValueError:
            n = 0

        res_cadenas.value = (
            f"• Concatenación (u + v): {concatenar_cadenas(u, v)}\n"
            f"• Inversión (u^R): {inversion_cadena(u)}\n"
            f"• Longitud (|u|): {longitud_cadena(u)}\n"
            f"• Potencia (u^{n}): {potencia_cadena(u, n)}"
        )
        page.update()

    btn_calc_cadenas = ft.ElevatedButton("Procesar Cadenas", on_click=calcular_cadenas)

    # Componentes para Operaciones con Lenguajes
    txt_lenguaje1 = ft.TextField(label="Lenguaje 1 (L1) - separados por coma", value="a, b", width=400)
    txt_lenguaje2 = ft.TextField(label="Lenguaje 2 (L2) - separados por coma", value="1, 2", width=400)
    txt_potencia_l = ft.TextField(label="Potencia (n)", value="2", width=150)
    res_lenguajes = ft.Text(value="Resultados de Lenguajes aparecerán aquí", size=16, weight=ft.FontWeight.BOLD)

    def calcular_lenguajes(e):
        l1 = {x.strip() for x in txt_lenguaje1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_lenguaje2.value.split(",") if x.strip()}
        try:
            n = int(txt_potencia_l.value or 0)
        except ValueError:
            n = 0

        res_lenguajes.value = (
            f"• L1: {l1}\n"
            f"• L2: {l2}\n"
            f"• Unión (L1 ∪ L2): {union_lenguajes(l1, l2)}\n"
            f"• Intersección (L1 ∩ L2): {interseccion_lenguajes(l1, l2)}\n"
            f"• Diferencia (L1 - L2): {diferencia_lenguajes(l1, l2)}\n"
            f"• Concatenación (L1 · L2): {concatenar_lenguajes(l1, l2)}\n"
            f"• Potencia (L1^{n}): {potencia_lenguaje(l1, n)}"
        )
        page.update()

    btn_calc_lenguajes = ft.ElevatedButton("Procesar Lenguajes", on_click=calcular_lenguajes)

    # Layout Principal en Tabs
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Operaciones con Cadenas",
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Procesamiento Formál de Cadenas", size=20, weight=ft.FontWeight.BOLD),
                        txt_cadena1,
                        txt_cadena2,
                        txt_potencia_k,
                        btn_calc_cadenas,
                        ft.Divider(),
                        res_cadenas
                    ], spacing=15),
                    padding=20
                )
            ),
            ft.Tab(
                text="Operaciones con Lenguajes",
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Procesamiento Formál de Lenguajes", size=20, weight=ft.FontWeight.BOLD),
                        txt_lenguaje1,
                        txt_lenguaje2,
                        txt_potencia_l,
                        btn_calc_lenguajes,
                        ft.Divider(),
                        res_lenguajes
                    ], spacing=15),
                    padding=20
                )
            )
        ],
        expand=1
    )

    page.add(
        ft.Text("Teoría de la Computación - Aplicación de Operaciones Básicas", size=24, weight=ft.FontWeight.BOLD),
        tabs
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")