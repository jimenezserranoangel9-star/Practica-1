# src/app.py
import flet as ft
from lenguajes import (
    obtener_prefijos, obtener_sufijos, obtener_subcadenas,
    generar_cerradura_kleene, generar_cerradura_positiva
)

def main(page: ft.Page):
    page.title = "Práctica 1 - Operaciones sobre Cadenas y Lenguajes"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # Funcionalidad para guardar archivos de texto
    def guardar_en_archivo(nombre_archivo, contenido):
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write(contenido)
            page.open(ft.SnackBar(ft.Text(f" Guardado exitosamente en: {nombre_archivo}")))
        except Exception as ex:
            page.open(ft.SnackBar(ft.Text(f" Error al guardar: {str(ex)}")))

    # --- TAB 1: OPERACIÓN 1 (Subcadenas, Prefijos, Sufijos) ---
    txt_cadena = ft.TextField(label="Cadena de entrada (w)", value="hola", width=300)
    res_op1 = ft.Text(value="Ingrese una cadena y presione 'Calcular'.", size=14)
    btn_export_op1 = ft.ElevatedButton(" Exportar a TXT", disabled=True)

    def procesar_op1(e):
        w = txt_cadena.value or ""
        pref = obtener_prefijos(w)
        suf = obtener_sufijos(w)
        sub = obtener_subcadenas(w)

        pref_str = [x if x != "" else "λ" for x in pref]
        suf_str = [x if x != "" else "λ" for x in suf]
        sub_str = [x if x != "" else "λ" for x in sub]

        texto_salida = (
            f"--- RESULTADOS OPERACIÓN 1 ---\n"
            f"Cadena evaluada: '{w}' (Longitud n = {len(w)})\n\n"
            f"1. Prefijos ({len(pref)}): {pref_str}\n"
            f"2. Sufijos ({len(suf)}): {suf_str}\n"
            f"3. Subcadenas distintas ({len(sub)}): {sub_str}\n"
        )
        res_op1.value = texto_salida
        
        btn_export_op1.disabled = False
        btn_export_op1.on_click = lambda _: guardar_en_archivo("operacion1_resultados.txt", texto_salida)
        page.update()

    btn_calc_op1 = ft.ElevatedButton("Calcular Prefijos/Sufijos/Subcadenas", on_click=procesar_op1)

    # --- TAB 2: OPERACIÓN 2 (Cerraduras Kleene y Positiva) ---
    txt_alfabeto = ft.TextField(label="Alfabeto Σ (separado por comas)", value="a, b", width=300)
    txt_nmax = ft.TextField(label="Longitud Máxima (n)", value="3", width=150)
    res_op2 = ft.Text(value="Ingrese alfabeto y longitud máxima.", size=14)
    btn_export_op2 = ft.ElevatedButton(" Exportar a TXT", disabled=True)

    def procesar_op2(e):
        raw_alfabeto = {x.strip() for x in txt_alfabeto.value.split(",") if x.strip()}
        try:
            n_max = int(txt_nmax.value or 0)
            kleene = generar_cerradura_kleene(raw_alfabeto, n_max)
            positiva = generar_cerradura_positiva(raw_alfabeto, n_max)

            kleene_str = [x if x != "" else "λ" for x in kleene]
            
            texto_salida = (
                f"--- RESULTADOS OPERACIÓN 2 ---\n"
                f"Alfabeto Σ = {raw_alfabeto}, Longitud máxima n = {n_max}\n\n"
                f"• Σ* ({len(kleene)} cadenas):\n{kleene_str}\n\n"
                f"• Σ+ ({len(positiva)} cadenas):\n{positiva}\n"
            )
            res_op2.value = texto_salida
            res_op2.color = None
            btn_export_op2.disabled = False
            btn_export_op2.on_click = lambda _: guardar_en_archivo("operacion2_resultados.txt", texto_salida)

        except ValueError as err:
            res_op2.value = f" Error: {str(err)}"
            res_op2.color = "red"
            btn_export_op2.disabled = True
        
        page.update()

    btn_calc_op2 = ft.ElevatedButton("Generar Cerraduras", on_click=procesar_op2)

    # Vistas de la App
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text="Operación 1: Subcadenas/Prefijos/Sufijos",
                content=ft.Container(
                    content=ft.Column([
                        txt_cadena,
                        ft.Row([btn_calc_op1, btn_export_op1]),
                        ft.Divider(),
                        res_op1
                    ], spacing=15), padding=20
                )
            ),
            ft.Tab(
                text="Operación 2: Cerraduras Kleene (*)/Positiva (+)",
                content=ft.Container(
                    content=ft.Column([
                        txt_alfabeto,
                        txt_nmax,
                        ft.Row([btn_calc_op2, btn_export_op2]),
                        ft.Divider(),
                        res_op2
                    ], spacing=15), padding=20
                )
            )
        ], expand=1
    )

    page.add(
        ft.Text("Teoría de la Computación - Aplicación Operaciones Básicas", size=22, weight=ft.FontWeight.BOLD),
        tabs
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")