# src/app.py
import flet as ft
from lenguajes import (
    obtener_prefijos, obtener_sufijos, obtener_subcadenas,
    generar_cerradura_kleene, generar_cerradura_positiva
)

def main(page: ft.Page):
    page.title = "Teoría de la Computación - Práctica 1"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    def guardar_en_archivo(contenido):
        try:
            with open("resultados_operaciones.txt", "w", encoding="utf-8") as f:
                f.write(contenido)
            page.open(ft.SnackBar(ft.Text("Resultados guardados en 'resultados_operaciones.txt'")))
        except Exception as ex:
            page.open(ft.SnackBar(ft.Text(f"Error al guardar: {str(ex)}")))

    # --- CAMPOS DE ENTRADA ---
    txt_alfabeto = ft.TextField(label="Alfabeto Σ (ej: a,b,c)", value="a,b,c", width=300)
    txt_nmax = ft.TextField(label="Máx. Combinaciones (n)", value="3", width=300)
    txt_cadena_ind = ft.TextField(label="Cadena Individual (w)", value="hola", width=300)
    txt_l1 = ft.TextField(label="Lenguaje 1 (L1)", value="ba,baa,b,ccc,aa", width=300)
    txt_l2 = ft.TextField(label="Lenguaje 2 (L2)", value="aa,aaa,baaa,ccc", width=300)

    # --- AUTÓMATA FINITO ---
    txt_estados = ft.TextField(label="Estados (ej: 0,1,2,3,4,5)", value="0,1,2,3,4,5", width=300)
    txt_est_init = ft.TextField(label="Estado Inicial", value="0", width=300)
    txt_est_acept = ft.TextField(label="Estados de Aceptación", value="4", width=300)
    txt_cad_validar = ft.TextField(label="Cadena a Validar", value="abbbacbcbcbcba", width=300)

    # --- SALIDA ---
    txt_resultado = ft.Text(value="Los resultados aparecerán aquí...", size=14, selectable=True, color="greenAccent")

    # --- FUNCIONES DE OPERACIONES ---
    def op_kleene(e):
        alf = {x.strip() for x in txt_alfabeto.value.split(",") if x.strip()}
        try:
            res = generar_cerradura_kleene(alf, int(txt_nmax.value or 0))
            txt_resultado.value = f"Cerradura de Kleene (Σ*):\n{res}"
        except Exception as err:
            txt_resultado.value = f"Error: {str(err)}"
        page.update()

    def op_positiva(e):
        alf = {x.strip() for x in txt_alfabeto.value.split(",") if x.strip()}
        try:
            res = generar_cerradura_positiva(alf, int(txt_nmax.value or 0))
            txt_resultado.value = f"Clausura Positiva (Σ+):\n{res}"
        except Exception as err:
            txt_resultado.value = f"Error: {str(err)}"
        page.update()

    def op_subcadenas(e):
        w = txt_cadena_ind.value or ""
        txt_resultado.value = (
            f"Cadena evaluada: '{w}'\n"
            f"• Prefijos: {obtener_prefijos(w)}\n"
            f"• Sufijos: {obtener_sufijos(w)}\n"
            f"• Subcadenas distintas: {obtener_subcadenas(w)}"
        )
        page.update()

    def op_concat_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Concatenación (L1 · L2):\n{{u + v for u in l1 for v in l2}}"
        page.update()

    def op_union_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Unión (L1 ∪ L2):\n{l1.union(l2)}"
        page.update()

    def op_inter_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Intersección (L1 ∩ L2):\n{l1.intersection(l2)}"
        page.update()

    def op_dif_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Diferencia (L1 - L2):\n{l1.difference(l2)}"
        page.update()

    def exportar_txt(e):
        guardar_en_archivo(txt_resultado.value)

    def validar_automata(e):
        estado_actual = txt_est_init.value.strip()
        estados_aceptacion = {x.strip() for x in txt_est_acept.value.split(",") if x.strip()}
        cadena = txt_cad_validar.value.strip()

        # Tabla simple de transiciones
        transiciones = {
            "0": {"a": "5", "b": "2", "c": "5"},
            "4": {"a": "5", "b": "5", "c": "5"},
            "5": {"a": "5", "b": "5", "c": "5"}
        }

        historial = [f"Estado inicial: q{estado_actual}"]
        for simbolo in cadena:
            if estado_actual in transiciones and simbolo in transiciones[estado_actual]:
                sig = transiciones[estado_actual][simbolo]
                historial.append(f"δ(q{estado_actual}, '{simbolo}') → q{sig}")
                estado_actual = sig
            else:
                historial.append(f"δ(q{estado_actual}, '{simbolo}') → q5 (Pozo)")
                estado_actual = "5"

        es_valida = estado_actual in estados_aceptacion
        res = f"=== EVALUACIÓN DE AUTÓMATA ===\nCadena: '{cadena}'\n"
        res += "\n".join(historial) + "\n\n"
        res += f"RESULTADO: {'¡CADENA ACEPTADA!' if es_valida else 'CADENA RECHAZADA (Estado final q' + estado_actual + ')'}"
        
        txt_resultado.value = res
        page.update()

    # --- LAYOUT EN COLUMNAS ---
    col_entradas = ft.Column([
        ft.Text("Entradas", size=18, weight=ft.FontWeight.BOLD),
        txt_alfabeto, txt_nmax, txt_cadena_ind, txt_l1, txt_l2
    ])

    col_botones = ft.Column([
        ft.Text("Operaciones", size=18, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton("Cerradura de Kleene", on_click=op_kleene, width=220),
        ft.ElevatedButton("Clausura Positiva", on_click=op_positiva, width=220),
        ft.ElevatedButton("Prefijos/Sufijos", on_click=op_subcadenas, width=220),
        ft.ElevatedButton("Concatenar Lenguajes", on_click=op_concat_l, width=220),
        ft.ElevatedButton("Unión de Lenguajes", on_click=op_union_l, width=220),
        ft.ElevatedButton("Intersección", on_click=op_inter_l, width=220),
        ft.ElevatedButton("Diferencia", on_click=op_dif_l, width=220),
        ft.ElevatedButton("Exportar a TXT", on_click=exportar_txt, width=220)
    ])

    col_automata = ft.Column([
        ft.Text("Autómata Finito", size=18, weight=ft.FontWeight.BOLD),
        txt_estados, txt_est_init, txt_est_acept, txt_cad_validar,
        ft.ElevatedButton("Validar Cadena en AF", on_click=validar_automata, width=220)
    ])

    page.add(
        ft.Text("Teoría de la Computación - Práctica 1", size=24, weight=ft.FontWeight.BOLD),
        ft.Row([col_entradas, col_botones, col_automata], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.START),
        ft.Divider(),
        ft.Container(content=txt_resultado, padding=10, bgcolor="black", border_radius=5)
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")