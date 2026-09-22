# src/app.py
import flet as ft
from lenguajes import (
    obtener_prefijos, obtener_sufijos, obtener_subcadenas,
    generar_cerradura_kleene, generar_cerradura_positiva
)

def main(page: ft.Page):
    page.title = "Teoría de la Computación - Operaciones sobre Lenguajes"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0D1117"  # Dark Mode estilo GitHub
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    def guardar_en_archivo(contenido):
        try:
            with open("resultados_operaciones.txt", "w", encoding="utf-8") as f:
                f.write(contenido)
            page.open(ft.SnackBar(ft.Text(" Resultados guardados exitosamente en 'resultados_operaciones.txt'"), bgcolor="green"))
        except Exception as ex:
            page.open(ft.SnackBar(ft.Text(f" Error al guardar: {str(ex)}"), bgcolor="red"))

    # --- ENCABEZADO ---
    header = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.TERMINAL, size=32, color="#58A6FF"),
                ft.Text("Teoría de la Computación", size=26, weight=ft.FontWeight.BOLD, color="#F0F6FC"),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("Plataforma Interactiva para Operaciones de Cadenas, Lenguajes y Autómatas", size=13, color="#8B949E")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=15, bgcolor="#161B22", border_radius=12, border=ft.border.all(1, "#30363D")
    )

    # --- COLUMNA IZQUIERDA: ENTRADAS DE CADENAS Y LENGUAJES ---
    txt_alfabeto = ft.TextField(label="Alfabeto Σ (ej: a,b,c)", value="a,b,c", border_color="#30363D", focused_border_color="#58A6FF")
    txt_nmax = ft.TextField(label="Máx. Combinaciones (n)", value="3", border_color="#30363D", focused_border_color="#58A6FF")
    txt_cadena_ind = ft.TextField(label="Cadena Individual (w)", value="hola", border_color="#30363D", focused_border_color="#58A6FF")
    txt_l1 = ft.TextField(label="Lenguaje 1 (L1)", value="ba,aaaaaaaaa,baa,b,ccc,aa", border_color="#30363D", focused_border_color="#58A6FF")
    txt_l2 = ft.TextField(label="Lenguaje 2 (L2)", value="aa,bababa,aaa,baaa,ccc,aaaaababa,bbbbbb", border_color="#30363D", focused_border_color="#58A6FF")

    card_entradas = ft.Container(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.INPUT, color="#58A6FF"), ft.Text("Entradas de Datos", size=16, weight=ft.FontWeight.BOLD, color="#F0F6FC")]),
            ft.Divider(color="#30363D"),
            txt_alfabeto, txt_nmax, txt_cadena_ind, txt_l1, txt_l2
        ], spacing=10),
        padding=15, bgcolor="#161B22", border_radius=12, border=ft.border.all(1, "#30363D"), expand=True
    )

    # --- SALIDA DE RESULTADOS ABAJO ---
    txt_resultado = ft.Text(value="Los resultados aparecerán aquí al presionar un botón...", size=14, color="#A3E635", selectable=True)
    
    box_resultado = ft.Container(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.ANALYTICS, color="#A3E635"), ft.Text("Salida de Operaciones / Evaluación", size=15, weight=ft.FontWeight.BOLD, color="#F0F6FC")]),
            ft.Divider(color="#30363D"),
            txt_resultado
        ]),
        padding=15, bgcolor="#0D1117", border_radius=12, border=ft.border.all(1, "#A3E635"), margin=ft.margin.only(top=15)
    )

    # --- FUNCIONES DE OPERACIONES SOBRE LENGUAJES ---
    def op_kleene(e):
        alf = {x.strip() for x in txt_alfabeto.value.split(",") if x.strip()}
        try:
            res = generar_cerradura_kleene(alf, int(txt_nmax.value or 0))
            txt_resultado.value = f"Cerradura de Kleene (Σ*):\n{res}"
        except Exception as err:
            txt_resultado.value = f" Error: {str(err)}"
        page.update()

    def op_positiva(e):
        alf = {x.strip() for x in txt_alfabeto.value.split(",") if x.strip()}
        try:
            res = generar_cerradura_positiva(alf, int(txt_nmax.value or 0))
            txt_resultado.value = f"Clausura Positiva (Σ+):\n{res}"
        except Exception as err:
            txt_resultado.value = f" Error: {str(err)}"
        page.update()

    def op_subcadenas(e):
        w = txt_cadena_ind.value or ""
        txt_resultado.value = (
            f"Cadena evaluada: '{w}'\n\n"
            f"• Prefijos ({len(obtener_prefijos(w))}): {obtener_prefijos(w)}\n"
            f"• Sufijos ({len(obtener_sufijos(w))}): {obtener_sufijos(w)}\n"
            f"• Subcadenas distintas ({len(obtener_subcadenas(w))}): {obtener_subcadenas(w)}"
        )
        page.update()

    def op_concat_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        res = {u + v for u in l1 for v in l2}
        txt_resultado.value = f"Concatenación de Lenguajes (L1 · L2):\n{res}"
        page.update()

    def op_union_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Unión de Lenguajes (L1 ∪ L2):\n{l1.union(l2)}"
        page.update()

    def op_inter_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Intersección de Lenguajes (L1 ∩ L2):\n{l1.intersection(l2)}"
        page.update()

    def op_dif_l(e):
        l1 = {x.strip() for x in txt_l1.value.split(",") if x.strip()}
        l2 = {x.strip() for x in txt_l2.value.split(",") if x.strip()}
        txt_resultado.value = f"Diferencia de Lenguajes (L1 - L2):\n{l1.difference(l2)}"
        page.update()

    def exportar_txt(e):
        guardar_en_archivo(txt_resultado.value)

    # --- COLUMNA CENTRO: BOTONES DE ACCIÓN ---
    def btn_estilo(texto, icono, funcion, color="#2563EB"):
        return ft.ElevatedButton(
            content=ft.Row([ft.Icon(icono, size=18), ft.Text(texto, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
            on_click=funcion,
            style=ft.ButtonStyle(color="#FFFFFF", bgcolor=color, shape=ft.RoundedRectangleBorder(radius=8), padding=12),
            width=260
        )

    card_botones = ft.Container(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.CALCULATE, color="#A855F7"), ft.Text("Operaciones", size=16, weight=ft.FontWeight.BOLD, color="#F0F6FC")]),
            ft.Divider(color="#30363D"),
            btn_estilo("Cerradura de Kleene", ft.Icons.AUTO_AWESOME, op_kleene, "#2563EB"),
            btn_estilo("Clausura Positiva", ft.Icons.ADD_CIRCLE_OUTLINE, op_positiva, "#2563EB"),
            btn_estilo("Prefijos / Sufijos", ft.Icons.FORMAT_LIST_BULLETED, op_subcadenas, "#0D9488"),
            btn_estilo("Concatenar Lenguajes", ft.Icons.LINK, op_concat_l, "#4F46E5"),
            btn_estilo("Unión de Lenguajes", ft.Icons.JOIN_FULL, op_union_l, "#4F46E5"),
            btn_estilo("Intersección", ft.Icons.JOIN_INNER, op_inter_l, "#4F46E5"),
            btn_estilo("Diferencia", ft.Icons.REMOVE_CIRCLE_OUTLINE, op_dif_l, "#4F46E5"),
            ft.Divider(color="#30363D"),
            btn_estilo("Exportar a TXT", ft.Icons.DOWNLOAD, exportar_txt, "#D97706")
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
        padding=15, bgcolor="#161B22", border_radius=12, border=ft.border.all(1, "#30363D"), expand=True
    )

    # --- COLUMNA DERECHA: EVALUADOR DE AUTÓMATA FINITO ---
    txt_estados = ft.TextField(label="Estados (ej: 0,1,2,3,4,5)", value="0,1,2,3,4,5", border_color="#30363D")
    txt_est_init = ft.TextField(label="Estado Inicial", value="0", border_color="#30363D")
    txt_est_acept = ft.TextField(label="Estados Aceptación (ej: 4)", value="4", border_color="#30363D")
    txt_cad_validar = ft.TextField(label="Cadena a Validar", value="abbbacbcbcbcba", border_color="#30363D")

    # Matriz de Transiciones por defecto (Estilo Anexo 1 del profesor)
    transiciones = {
        "0": {"a": "5", "b": "2", "c": "5"},
        "4": {"a": "5", "b": "5", "c": "5"},
        "5": {"a": "5", "b": "5", "c": "5"}
    }

    def validar_automata(e):
        estado_actual = txt_est_init.value.strip()
        estados_aceptacion = {x.strip() for x in txt_est_acept.value.split(",") if x.strip()}
        cadena = txt_cad_validar.value.strip()

        historial = [f"Estado inicial: q{estado_actual}"]
        
        # Simulación del paso a paso por los estados
        error = False
        for simbolo in cadena:
            if estado_actual in transiciones and simbolo in transiciones[estado_actual]:
                siguiente_estado = transiciones[estado_actual][simbolo]
                historial.append(f"δ(q{estado_actual}, '{simbolo}') → q{siguiente_estado}")
                estado_actual = siguiente_estado
            else:
                # Si no hay transición explícita, por defecto va a pozo (5) o se rechaza
                historial.append(f"δ(q{estado_actual}, '{simbolo}') → Tránsito no definido (Rechazada)")
                error = True
                break

        es_aceptada = (estado_actual in estados_aceptacion) and not error

        res_texto = f"=== EVALUACIÓN DE AUTÓMATA FINITO ===\n"
        res_texto += f"Cadena evaluada: '{cadena}'\n"
        res_texto += "Recorrido de transiciones:\n  " + "\n  ".join(historial) + "\n\n"
        
        if es_aceptada:
            res_texto += f" RESULTADO: ¡CADENA ACEPTADA! El estado final q{estado_actual} es de aceptación."
        else:
            res_texto += f" RESULTADO: CADENA RECHAZADA. El estado final q{estado_actual} NO es un estado de aceptación ({estados_aceptacion})."

        txt_resultado.value = res_texto
        page.update()

    card_automata = ft.Container(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.ACCOUNT_TREE, color="#EC4899"), ft.Text("Definición de Autómata", size=16, weight=ft.FontWeight.BOLD, color="#F0F6FC")]),
            ft.Divider(color="#30363D"),
            txt_estados, txt_est_init, txt_est_acept,
            ft.Text("Transiciones Registradas:", size=13, weight=ft.FontWeight.BOLD, color="#8B949E"),
            ft.Container(
                content=ft.Column([
                    ft.Text("• 0: a → 5 | b → 2 | c → 5", size=12, color="#C9D1D9"),
                    ft.Text("• 4: a → 5 | b → 5 | c → 5", size=12, color="#C9D1D9"),
                    ft.Text("• 5: a → 5 | b → 5 | c → 5", size=12, color="#C9D1D9")
                ]), padding=10, bgcolor="#0D1117", border_radius=6
            ),
            txt_cad_validar,
            ft.ElevatedButton("Validar Cadena en AF", icon=ft.Icons.PLAY_ARROW, on_click=validar_automata, style=ft.ButtonStyle(bgcolor="#EC4899", color="white"), width=280)
        ], spacing=10),
        padding=15, bgcolor="#161B22", border_radius=12, border=ft.border.all(1, "#30363D"), expand=True
    )

    # Layout de 3 Columnas
    grid = ft.Row([
        card_entradas,
        card_botones,
        card_automata
    ], vertical_alignment=ft.CrossAxisAlignment.START, spacing=15)

    page.add(
        header,
        ft.Container(height=10),
        grid,
        box_resultado
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")