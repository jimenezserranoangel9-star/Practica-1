# src/app.py
import flet as ft
from lenguajes import (
    obtener_prefijos, obtener_sufijos, obtener_subcadenas,
    generar_cerradura_kleene, generar_cerradura_positiva
)

def main(page: ft.Page):
    page.title = "Operaciones sobre Lenguajes y Autómatas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1100
    page.window_height = 800
    page.padding = 15

    # Funcionalidad para exportar/guardar en archivo de texto
    def guardar_en_archivo(contenido):
        try:
            with open("resultados_operaciones.txt", "w", encoding="utf-8") as f:
                f.write(contenido)
            page.open(ft.SnackBar(ft.Text(" Resultados guardados en 'resultados_operaciones.txt'")))
        except Exception as ex:
            page.open(ft.SnackBar(ft.Text(f" Error al guardar: {str(ex)}")))

    # --- COLUMNA IZQUIERDA: INPUTS DE CADENAS Y LENGUAJES ---
    txt_alfabeto = ft.TextField(label="Ingrese el alfabeto separado por comas (ej: a,b,c)", value="a,b,c", width=320, dense=True)
    txt_nmax = ft.TextField(label="Ingrese el número máximo de combinaciones", value="3", width=320, dense=True)
    txt_cadena_ind = ft.TextField(label="Ingrese una cadena (para prefijos/sufijos/subcadenas)", value="hola", width=320, dense=True)
    txt_l1 = ft.TextField(label="Ingrese las cadenas del primer lenguaje separadas por comas", value="ba,aaaaaaaaa,baa,b,ccc,aa", width=320, dense=True)
    txt_l2 = ft.TextField(label="Ingrese las cadenas del segundo lenguaje separadas por comas", value="aa,bababa,aaa,baaa,ccc,aaaaababa,bbbbbb", width=320, dense=True)
    txt_pot_l = ft.TextField(label="Ingrese la potencia del lenguaje", value="3", width=320, dense=True)

    # Area de Resultados Abajo
    txt_resultado = ft.Text(value="Resultados de las operaciones...", size=13, weight=ft.FontWeight.W_500, color="greenAccent")

    # Callbacks de Operaciones
    def op_kleene(e):
        alf = {x.strip() for x in txt_alfabeto.value.split(",") if x.strip()}
        try:
            res = generar_cerradura_kleene(alf, int(txt_nmax.value or 0))
            txt_resultado.value = f"Cerradura de Kleene (Σ*): {res}"
        except Exception as err:
            txt_resultado.value = f"Error: {str(err)}"
        page.update()

    def op_positiva(e):
        alf = {x.strip() for x in txt_alfabeto.value.split(",") if x.strip()}
        try:
            res = generar_cerradura_positiva(alf, int(txt_nmax.value or 0))
            txt_resultado.value = f"Clausura Positiva (Σ+): {res}"
        except Exception as err:
            txt_resultado.value = f"Error: {str(err)}"
        page.update()

    def op_subcadenas(e):
        w = txt_cadena_ind.value or ""
        txt_resultado.value = (
            f"Cadena '{w}' -> Prefijos: {obtener_prefijos(w)} | "
            f"Sufijos: {obtener_sufijos(w)} | "
            f"Subcadenas: {obtener_subcadenas(w)}"
        )
        page.update()

    def op_concat_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        res = {u + v for u in l1 for v in l2}
        txt_resultado.value = f"Concatenar lenguajes (L1 · L2): {res}"
        page.update()

    def op_union_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Unión de lenguajes (L1 ∪ L2): {l1.union(l2)}"
        page.update()

    def op_inter_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Intersección de lenguajes (L1 ∩ L2): {l1.intersection(l2)}"
        page.update()

    def op_dif_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Diferencia de lenguajes (L1 - L2): {l1.difference(l2)}"
        page.update()

    def exportar_txt(e):
        guardar_en_archivo(txt_resultado.value)

    # --- COLUMNA CENTRAL: MENÚ DE BOTONES DE ACCIÓN ---
    col_botones = ft.Column([
        ft.ElevatedButton("Cerradura de Kleene", on_click=op_kleene, width=220),
        ft.ElevatedButton("Clausura Positiva", on_click=op_positiva, width=220),
        ft.ElevatedButton("Prefijos/Sufijos/Subcadenas", on_click=op_subcadenas, width=220),
        ft.ElevatedButton("Concatenar lenguajes", on_click=op_concat_l, width=220),
        ft.ElevatedButton("Unión de lenguajes", on_click=op_union_l, width=220),
        ft.ElevatedButton("Intersección de lenguajes", on_click=op_inter_l, width=220),
        ft.ElevatedButton("Diferencia de lenguajes", on_click=op_dif_l, width=220),
        ft.ElevatedButton(" Exportar Resultados a TXT", on_click=exportar_txt, width=220, color="orangeAccent"),
    ], spacing=8, alignment=ft.MainAxisAlignment.CENTER)

    # --- COLUMNA DERECHA: CONFIGURACIÓN DE AUTÓMATAS ---
    txt_estados = ft.TextField(label="Ingrese los estados separados por comas (ej: 0,1,2)", value="0,1,2,3,4,5", width=300, dense=True)
    txt_est_init = ft.TextField(label="Ingrese el estado inicial", value="0", width=300, dense=True)
    txt_est_acept = ft.TextField(label="Ingrese los estados de aceptación separados por comas", value="4", width=300, dense=True)
    txt_cad_validar = ft.TextField(label="Ingrese la cadena a validar", value="abbbacbcbcbcba", width=300, dense=True)
    
    col_derecha = ft.Column([
        txt_estados,
        txt_est_init,
        txt_est_acept,
        ft.Text("Definir Transiciones", weight=ft.FontWeight.BOLD),
        ft.Row([ft.Text("0: a -> 5"), ft.Text("0: b -> 2"), ft.Text("0: c -> 5")], spacing=15),
        ft.Row([ft.Text("4: a -> 5"), ft.Text("4: b -> 5"), ft.Text("4: c -> 5")], spacing=15),
        ft.Row([ft.Text("5: a -> 5"), ft.Text("5: b -> 5"), ft.Text("5: c -> 5")], spacing=15),
        txt_cad_validar,
        ft.ElevatedButton("Validar Cadena", width=300)
    ], spacing=10)

    col_izquierda = ft.Column([
        txt_alfabeto,
        txt_nmax,
        txt_cadena_ind,
        txt_l1,
        txt_l2,
        txt_pot_l
    ], spacing=10)

    # Layout Principal de 3 Columnas igualito al Anexo 1
    layout_3_columnas = ft.Row([
        col_izquierda,
        col_botones,
        col_derecha
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.START)

    page.add(
        layout_3_columnas,
        ft.Divider(),
        ft.Container(
            content=txt_resultado,
            padding=10,
            bgcolor=ft.Colors.GREY_900,
            border_radius=5,
            width=1050
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")