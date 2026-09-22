import flet as ft

def main(page: ft.Page):
    page.title = "Operaciones basicas sobre lenguajes"
    entrada = ft.TextField(label="Cadena")
    salida = ft.Text()
    def calcular(e):
        salida.value = entrada.value
        page.update()

    page.add(entrada, ft.ElevatedButton("Prefijos", on_click=calcular), salida)

ft.run(main)
